import shutil
import os
import string
from typing import Union
from fastapi import FastAPI, UploadFile, File
from collections import defaultdict
from fileinput import filename
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from extractPDF import ExtractPDF

app = FastAPI()
dirname = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(dirname, 'uploads')

@app.post("/convertPDF")
async def uploadPDF(file: UploadFile = File (...)):
    path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    question_title = defaultdict(list)
    question_content = defaultdict(list)
    answer_title = defaultdict(list)
    answer_content = defaultdict(list)
    explain_list = defaultdict(list)
    correct_answers = ['blank']

    data = ExtractPDF.extract_pdf(path, "")       
    titles =  data["titles"]
    for key in titles:
        question_title[key].append(titles[key][4])
        
    questions = data["questions"]
    for key in questions:
        question = questions[key]
        for q in question:
            question_content[key].append(q["coor"][4])
        
    answers = data["answers"]
    for key in answers:
        options = answers[key]["options"]
        for option in options:
            answer_title[key].append(option[4])
            answer_content[key].append(option[9])
    
    explains = data["explains"]
    for key in explains:
        explain = explains[key]
        for e in explain:
            explain_list[key].append(e[4])
    
    correct_list = data["correct_options"]
    for key in correct_list:
        correct_answers.append(correct_list[key])
        
    return {"question_title": question_title, "question_content": question_content, "answer_title": answer_title, "answer_content": answer_content, "explain_list":explain_list, "correct_answers": correct_answers}