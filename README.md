# Pythagorean-triplets
A lightweight Python script to find and count Pythagorean triplets up to a given number N efficiently.

# Pythagorean Triplet Finder

A simple, optimized Python script that finds and counts all [Pythagorean triplets](https://en.wikipedia.org/wiki/Pythagorean_triple) ($a^2 + b^2 = c^2$) up to a user-defined limit $N$.

## 🚀 Features
* **Mathematical Optimization:** Uses square roots (`** 0.5`) to eliminate an entire nested loop, improving performance.
* **Duplicate Prevention:** The inner loop starts at `a` to ensure unique triplets (e.g., finding `3 4 5` without repeating `4 3 5`).
* **Boundary Control:** Ensures all numbers in the triplet ($a, b, c$) remain within the user's limit $N$.

## 💻 How to Run

1. Make sure you have Python installed.
2. Clone this repository.

##EXAMPLE OUTPUT
N = 20
3 4 5
5 12 13
6 8 10
8 15 17
9 12 15
Total triplets found: 5

here are 16 primitive Pythagorean triples of numbers up to 100:

+-----+-----+-----+
|  a  |  b  |  c  |
+-----+-----+-----+
|   3 |   4 |   5 |
|   5 |  12 |  13 |
|   8 |  15 |  17 |
|   7 |  24 |  25 |
|  20 |  21 |  29 |
|  12 |  35 |  37 |
|   9 |  40 |  41 |
|  28 |  45 |  53 |
|  11 |  60 |  61 |
|  16 |  63 |  65 |
|  33 |  56 |  65 |
|  48 |  55 |  73 |
|  13 |  84 |  85 |
|  36 |  77 |  85 |
|  39 |  80 |  89 |
|  65 |  72 |  97 |
+-----+-----+-----+
Other small Pythagorean triples such as (6, 8, 10) are not listed because they are not primitive; for instance (6, 8, 10) is a multiple of (3, 4, 5).

Each of these points (with their multiples) forms a radiating line in the scatter plot to the right.

These are the remaining primitive Pythagorean triples of numbers up to 300:

+-----+-----+-----+
|  a  |  b  |  c  |
+-----+-----+-----+
|  20 |  99 | 101 |
|  60 |  91 | 109 |
|  15 | 112 | 113 |
|  44 | 117 | 125 |
|  88 | 105 | 137 |
|  17 | 144 | 145 |
|  24 | 143 | 145 |
|  51 | 140 | 149 |
|  85 | 132 | 157 |
| 119 | 120 | 169 |
|  52 | 165 | 173 |
|  19 | 180 | 181 |
|  57 | 176 | 185 |
| 104 | 153 | 185 |
|  95 | 168 | 193 |
|  28 | 195 | 197 |
|  84 | 187 | 205 |
| 133 | 156 | 205 |
|  21 | 220 | 221 |
| 140 | 171 | 221 |
|  60 | 221 | 229 |
| 105 | 208 | 233 |
| 120 | 209 | 241 |
|  32 | 255 | 257 |
|  23 | 264 | 265 |
|  96 | 247 | 265 |
|  69 | 260 | 269 |
| 115 | 252 | 277 |
| 160 | 231 | 281 |
| 161 | 240 | 289 |
|  68 | 285 | 293 |
+-----+-----+-----+

