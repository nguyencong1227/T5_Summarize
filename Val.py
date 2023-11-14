# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:39:39 2023

@author: nguyencong1227
"""

from rouge_score import rouge_scorer

# INput
reference_summary_path = "reference_summary.txt"  
model_summary_path = "model_summary.txt"  


with open(reference_summary_path, "r", encoding="utf-8") as reference_file:
    reference_summary = reference_file.read()

with open(model_summary_path, "r", encoding="utf-8") as model_file:
    model_summary = model_file.read()

# create scorer ROUGE
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)

# ROUGE
scores = scorer.score(reference_summary, model_summary)

print("ROUGE Scores:")
print(f"ROUGE-1 Score: {scores['rouge1'].fmeasure}")
print(f"ROUGE-2 Score: {scores['rouge2'].fmeasure}")
print(f"ROUGE-L Score: {scores['rougeL'].fmeasure}")

