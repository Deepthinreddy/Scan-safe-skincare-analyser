# ScanSafe – AI Skincare Ingredient Analyzer

## Overview

ScanSafe is a skincare ingredient analysis tool that helps users understand the safety of cosmetic product ingredients.

Many skincare products contain complex chemical ingredient lists that are difficult for consumers to interpret. ScanSafe analyzes ingredient lists and identifies potentially harmful or irritating components using a curated ingredient safety database.

The goal is to provide **transparent ingredient insights** so consumers can make safer skincare choices.

---

## Problem

Most consumers cannot easily understand cosmetic ingredient labels.

Ingredients such as **fragrance, parabens, or sulfates** may cause irritation or other issues for certain skin types, but they are often hidden in long and technical ingredient lists.

While existing apps like Yuka or ThinkDirty attempt to evaluate products, the decision process behind their ratings is often unclear.

---

## Solution

ScanSafe analyzes ingredient lists and compares them with a safety database to classify ingredients into different safety categories.

The system highlights potentially harmful ingredients and generates a simplified safety summary.

---

## Features

• Ingredient list analysis
• Detection of potentially harmful ingredients
• Safety classification for each ingredient
• Easy-to-understand output summary
• Transparent ingredient analysis logic

---

## Example

Input Ingredient List:

Water, Niacinamide, Glycerin, Fragrance, Sodium Lauryl Sulfate

Analysis Result:

Safe Ingredients
Water
Niacinamide
Glycerin

Potential Irritants
Fragrance
Sodium Lauryl Sulfate

Safety Score: 6 / 10

---

## Tech Stack

Python
Pandas
Natural Language Processing
Ingredient Safety Dataset

---

## System Workflow

User enters ingredient list
↓
Ingredients parsed
↓
Database lookup
↓
Safety classification
↓
Result summary generated

---

## Project Structure

data
 ingredient_database.csv

src
 analyzer.py

images
 demo.png

README.md
requirements.txt

---

## How to Run

Clone the repository

git clone https://github.com/Deepthinreddy/Scan-safe-skincare-analyser

Install dependencies

pip install -r requirements.txt

Run the analyzer

python analyzer.py

---

## Future Improvements

• OCR scanning from product images
• Mobile application version
• Personalized skincare recommendations
• Dermatologist-verified ingredient database
• Integration with product barcode scanning

---

## Motivation

This project was created to explore how **AI and data analysis can help consumers better understand skincare products** and make informed decisions about the ingredients they apply to their skin.

