using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

namespace Mystilink.Liuyao
{
    /// <summary>
    /// Invokes the liuyao CLI and returns JSON stdout.
    /// </summary>
    public static class LiuyaoCalculator
    {
        public static string ResolveCli()
        {
            var env = Environment.GetEnvironmentVariable("MYSTILINK_LIUYAO_CLI");
            return string.IsNullOrWhiteSpace(env) ? "liuyao" : env;
        }

        public static string Run(params string[] args)
        {
            var psi = new ProcessStartInfo
            {
                FileName = ResolveCli(),
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                UseShellExecute = false,
                CreateNoWindow = true,
                StandardOutputEncoding = Encoding.UTF8,
                StandardErrorEncoding = Encoding.UTF8,
            };
            foreach (var a in args)
            {
                psi.ArgumentList.Add(a);
            }

            using var proc = Process.Start(psi)
                ?? throw new InvalidOperationException("Failed to start liuyao");
            string stdout = proc.StandardOutput.ReadToEnd();
            string stderr = proc.StandardError.ReadToEnd();
            proc.WaitForExit();
            if (proc.ExitCode != 0)
            {
                var msg = string.IsNullOrWhiteSpace(stderr) ? stdout : stderr;
                throw new InvalidOperationException(
                    string.IsNullOrWhiteSpace(msg)
                        ? $"liuyao exited with code {proc.ExitCode}"
                        : msg.Trim());
            }
            return stdout;
        }

        public static string Cast(int? seed = null, string? throws = null)
        {
            var args = new List<string> { "cast" };
            if (!string.IsNullOrEmpty(throws))
            {
                args.Add("--throws");
                args.Add(throws);
            }
            else if (seed.HasValue)
            {
                args.Add("--seed");
                args.Add(seed.Value.ToString());
            }
            return Run(args.ToArray());
        }

        public static string Version()
        {
            return Run("version");
        }
    }
}
