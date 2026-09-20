package com.mystilink.liuyao;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

/**
 * Invokes the liuyao CLI and returns JSON stdout.
 */
public final class LiuyaoCalculator {
    private LiuyaoCalculator() {}

    public static String resolveCli() {
        String env = System.getenv("MYSTILINK_LIUYAO_CLI");
        if (env != null && !env.isBlank()) {
            return env;
        }
        return "liuyao";
    }

    public static String run(String... args) throws Exception {
        List<String> cmd = new ArrayList<>();
        cmd.add(resolveCli());
        for (String a : args) {
            cmd.add(a);
        }
        ProcessBuilder pb = new ProcessBuilder(cmd);
        pb.redirectErrorStream(false);
        Process proc = pb.start();
        StringBuilder stdout = new StringBuilder();
        StringBuilder stderr = new StringBuilder();
        try (BufferedReader out = new BufferedReader(
                new InputStreamReader(proc.getInputStream(), StandardCharsets.UTF_8));
             BufferedReader err = new BufferedReader(
                new InputStreamReader(proc.getErrorStream(), StandardCharsets.UTF_8))) {
            String line;
            while ((line = out.readLine()) != null) {
                stdout.append(line).append('\n');
            }
            while ((line = err.readLine()) != null) {
                stderr.append(line).append('\n');
            }
        }
        int code = proc.waitFor();
        if (code != 0) {
            String msg = stderr.length() > 0 ? stderr.toString() : stdout.toString();
            if (msg.isBlank()) {
                msg = "liuyao exited with code " + code;
            }
            throw new IllegalStateException(msg.trim());
        }
        return stdout.toString();
    }

    public static String cast(Integer seed, String throwsCsv) throws Exception {
        List<String> args = new ArrayList<>();
        args.add("cast");
        if (throwsCsv != null && !throwsCsv.isEmpty()) {
            args.add("--throws");
            args.add(throwsCsv);
        } else if (seed != null) {
            args.add("--seed");
            args.add(String.valueOf(seed));
        }
        return run(args.toArray(new String[0]));
    }

    public static String version() throws Exception {
        return run("version");
    }
}
