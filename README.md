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
