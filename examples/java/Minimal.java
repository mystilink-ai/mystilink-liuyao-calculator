package com.mystilink.liuyao.examples;

import com.mystilink.liuyao.LiuyaoCalculator;

public class Minimal {
    public static void main(String[] args) throws Exception {
        String json = LiuyaoCalculator.cast(123, null);
        System.out.println(json);
    }
}
