<h1 align-text="center">PDF2ExamApi - PDF Examination 
Question Extraction Tool
</h1>

##  Features
PDF2Exam: Đây đơn giản là 1 tool để convert đề pdf thành dạng ảnh (base64image)
Toàn bộ code được tôi sử dụng ở đây đều thuộc về github này: https://github.com/edmicro-tech/PDF2Exam (xin cảm ơn tác giả rất nhiều) </br>
Vậy vì sao có PDF2ExamApi?</br>
Vì tôi là 1 dev .net nên rất khó để áp dụng được tool của tác giả vào phần mềm của mình, vì vậy tôi học cách viết python (trong khoảng 2h) 
và trả về dưới dạng api để có thể đáp ứng được yêu cầu của mình.</br>
(*) Lưu ý: Phần code này có thể có rất nhiều bug do tôi mới học ngôn ngữ python đc vài giờ, và chỉ để đáp ứng đc yêu cầu công việc của tôi!

##  Setup
Install Python 3. </br>
Install fitz.
```sh
pip3 install fitz
pip install python-multipart   
pip install --user uvicorn 
pip install fastapi
```

Install all requirements.
```sh
pip3 install -r requirements.txt 
```


##  How to run 
Run the command below.
```sh
uvicorn main:app --reload
```

Go to "http://127.0.0.1:8000/docs". Click "Try it out" choosen file and then hit "Submit." PDF2ExamApi will make a copy of your file in the folder uploads. 

![Upload image](/images/images01.png)

After the file finishes processing, they will return to json data.

![Display image](/images/images02.png)


###  Json data return

```sh
{
  "question_title": {
    "question_1": [
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADcAAAAZCAIAAAAaHyFXAAAACXBIWXMAAA7EAAAOxAGVKw4bAAADgElEQVR4nO2WS0hyWxiGX+3PMFPIG5mBRFAWEUVCNbELIplBUmEQFRjhtBwWaWBNbN6o6GaNjKJB10HDQsKBRuAoQQ0RtEwluqDrDHan0zE9R/9f/tOB3tFea717rWd9+1vfXjRCCL686P81QFb6psyfvinzp79R3t7eWq3WycnJiYkJk8nkcDgArKysvLy8vHv0ej2Px9Pr9b+4cCKRsNlse3t7WbnJn1paWiouLlapVB6PhxByfX2tUCiEQiGNRovH45SHmrSnpwfA7u4u+Snd3d1ZLJaKigoAMzMz2bzyRmkwGABUVlY+PT29jyWTSY1GA4CiDAaDIpFoa2uLEGK1WsvKygKBQK6Ibrd7fn5ep9NRMcqB0m6302g0ACaTKWX44eGBy+VSlH6/3+12f1zP5/PlSknJ6XTmRPkDgNlsJoQAUCgUKfnA4XCWl5cZDAYANpu9vb3t9Xo9Ho9YLNbpdDU1NQA2NjZcLheAxsbG0dHRubm5eDwOoLm5eXh4OG2aFRUVZZ/Bb3kpEomo54+hSlEymWxoaJDJZISQcDhcUlICYGdnhxDy+PhYWloKoL+/nxASjUZZLBYArVabaTa3251TLOmRSCQQCFDv8Hi8TJvxer0ul8vhcITDYS6X29bWBmB1dRUAk8l83ycVcrFYnFuo/k0/2Gw2g8Ggak0sFuPz+Wl9EonEaDQyGAwejxeJRKLRKIBIJJJfmkyiFxQU1NXVUY1QKPQPVrPZLJPJ1Gr11NRULBb7LXhvogNQq9VU4/z8PJPv9fVVo9GoVKru7u719XWq2uVdJMM1kg7AaDRWV1cDWFtbSyQSKXAjIyM+n29zc3N/fx9Ab2/v51kKCwspc5Y0yWTyM9bBwQGfz1cqlWlYqUPkcrmkUimAvr6+UChEddrt9s7OTuogLy4uUv7x8XGLxSIQCABIJBKn00kIGRsbAyAQCE5PTy0WC5PJBFBbWxsMBtOeWZvNRs32sQ4MDg5SnVdXVyn+v/6Qz8/PCwsLra2tbDZbKpWWl5cPDAy816b7+/uuri4Wi9XS0nJ8fHx4eCgUCuvr6y8uLgghfr+/o6ODxWI1NTWdnJwolUqtVjs9PX10dJSy3s3NzezsrEKhkMvlcrm8vb3dYDBcXl4SQs7OzqqqqoaGhj7vipY2FaLRKIfDyfLz/Qalp/xq+h/eL7+svinzpz8AVgt0kn1XjLEAAAAASUVORK5CYII="
    ]
  },
  "question_content": {
    "question_1": [
      "data:image/png;base64,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"
    ]
  },
  "answer_title": {
    "question_1": [
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAZCAIAAAC6gEm5AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABP0lEQVR4nO2UoYsCQRjF3xwGo1rEYjGajIospgXBYtRsERG2+V8I2kQNajKKoM0qimJZDIJgMxkMysLKPIPDyXrHsWq5g3tMmW+YH+973zCCJN7Tx5v3/xE/IrZbdDpPMuiUYchQSNo23cuBsCz6/RJgv/8qotslQICJhHwRkcnIeFzeKKuVW8Q9TtNEJALDELdtve764X/CikVpmrRtBoMSoNcrD4dnXJzP2GwQjcLjQaEAAJYl2m1XJgRJAK0Wej2mUgCw36PZFADCYe52Qgh3jSSTcjrlYqGWrqtQBwOHZ/ndoEByNmM+7zgcjdR0Ne1e13UZCMjh8AvicmE6LWs1R/V4VAiAkwlJrtdqm80+OvFUKjydMB5TCFEuA8ByiUaDmqY6rVbh84lYDLkc53OUSo/ZqDjf0e/8L/4s4grYogIsff9i9wAAAABJRU5ErkJggg==",
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAZCAIAAAC6gEm5AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABZklEQVR4nO2Uv64BQRjFz7DNJiIkCpGNiEbjBRQ0CoVKodH7U3gDT+AR1JpV6ChEvAChVAgJFVFJRKLxnVvs5oq1N1Yo75cpZr7M/HLOmckokvisfB+e/0c8lDYYYLe7r5VCMIhYDJkMdN0b43xmqyUAAUajsliw32cgIIGAtNv0UiC5XtNC5HJidet1Gzoev0b4AGiaU1oyqazJbPbah3uch4P9ZDMZD1mQ3G7vRi4XjkYMhSSRENP0lMWDh80GzSbnc1yvKBaRTnuQ8KzCAjebAtDvl17P2408I/Z7uxMKiYiHG3muaBR+PwGcTup0+tXr7sMdcTzidlMA0mmGwwBQKDAS4WDwRxbDoS07HhcR3m6s1QSgYchqRZLLpb2hVHJxpbpdmibPZ5sYiUDXEQwim1Xl8v3VVSqcTtHpqHzeKULx449Pm0zeO2AYSKWcTb41Gg1nHFq1+p6RXE45Ol/I4gsf3w9+h5u0CnkWJgAAAABJRU5ErkJggg==",
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAZCAIAAAC6gEm5AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABWklEQVR4nO2Uu4rCUBCG5+iSQohFBEE7ESTYWNjYCiJIiihWIvgOvoCVr2DnI2hlKxYWQsBKUOwEQWxSeIUYZP4tzOKFeFm3sdi/G2bOxznzzxkBgP4mzx/P/yOu9HUZLBbU69FwiP2ewmHSdZFMUrNJlQpJ0n0GftRowOfjXI5nMwAYj5HJcDDIQvBuhwdyENUqEyESYcs655iRzzMRniMMA0IwEWo1vkmv11CUF26haUwEIvT7LhXtNmz7GSIUchDT6aPSe/KsVrRcilNrA4F3TPXIMkmS89O227cQXi/F405gmm8hiEjTnGAweFLtvhgAWBZiMSZCIsHH41WrbBvlMs/nAJDNsqJwp+PmCIDRCKrKRNB1Nk0nZxhIp7nVAoDJBCfXCoXb2TkP+OGAeh2pFMsyqyqHw1ws8qXNpRJHo9zt3t5CwO19mw35/a+20x3xK33GyvkMxDdbieTzaq7IwAAAAABJRU5ErkJggg==",
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAZCAIAAAC6gEm5AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABNUlEQVR4nO2Uv4rCQBjEZ/VIIWqaYGEhCAqBgJWCrYhai2Bh6xv4DnZ2QvwDPoJgYS3Y2ooWWqewU4goCDtXZDku3olHbK5wqmH49rfLMnyCJF5T6MXzb4RPH7MZHOcbMoRkEtksMhlo2t8YxyPbbQkQoGnK5ZLjMQsFGY3KbpfXK58KJBcLeohmU3rp6UTTlAAtS14uTxAh7/F3isfR6wkAm43odJ507+F3ViqIRAhgMIDrBkJoGlIpz4r1OhACQCKhzH4fFHE+K5NOB0V89SWXC4RwHBwOANBoUNdV+OtieIiYTEAKw+BwKLykVqNhcD7/MUrStlW1ikVJ0nXZ7zMclqWS3O1Uf7ZbNVOvy7tqCdvmdMrbTRF1HbEYLEvk86hWfZe1WlytMBqJctmXi/fi+2eIT5Bi1jUXQchMAAAAAElFTkSuQmCC"
    ]
  },
  "answer_content": {
    "question_1": [
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJ8AAAAZCAIAAACgkGtyAAAACXBIWXMAAA7EAAAOxAGVKw4bAAABFUlEQVR4nO3aMYqEMBiGYbOzIFoL2pkD5BgeQCwsPZJHSaOXEDvFQjyCVoOgpMkWCzNTTLFZEgZ/vqcSFfnhRY0g01p7QNTXpwcAh1CXMtSlDHUpQ13KUJey/9SdpmkYBuujgHVmdbuuy/NcCNH3vaOBwCKDusdxJElSVZW7acAug7pBEKRpGsexu2nALqyqKENdylCXsu/HVl3X+76/PYlzjsXUFT3rcs7P83x7ElZSF/WsWxTFB+cAF+y8d5VSZVlKKa1cDWwxrjvPs+d5y7K87ty2TUrZtq21ucAG9vc/b7TWTdOM46iU8n1fCJFlWRiGv0fXdY2iiDHmbFQwZlAXLgffu2Td76hL1+2GJzNpuHcp+wG/kEm/dnUgqAAAAABJRU5ErkJggg==",
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJUAAAAZCAIAAAC3svu7AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA4klEQVR4nO3aMQqDMBjF8S+lm5DFk7iIs7t7DiMex8E5eBIHBy8gOIlTQOygtFQ6qKUND95vyZLhwX/JELUsixCsm+8B9BX2w8Z+2NgPG/thYz9s+37W2r7vvUyhC1796rqO4zjLsmEYPA6iU7Z+4zgmSWKM8buGzrqvh9ZaRMIw9DqGTuP7BRv7YWM/bOyHjf2wsR+2Q/2Kosjz/NdT6IK3fm3bikjXdbtLVVWVZfm/UXSYWv9POOestU3TzPOstY6iKE3T56VpmpRSQRD420mfKf5/gcb3Czb2w8Z+2NgP2wOKFzRSHSXdGgAAAABJRU5ErkJggg==",
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJUAAAAZCAIAAAC3svu7AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABi0lEQVR4nO3Zv6qCUBwH8M41iiaXfIOgoXIsGm3oEdoanHqDHqDZqVEwaHSoQWgKGgpqCKShaGtzOuDipoN3kNsfb3KrC0cPfD+THhy+8D3I+SkJwzAH3PpKOwD8C/rjG/rjG/rjG/rjG/rjGKW5fGxJ07Tz+Rxde543nU5LpRLzYPAS133s73K5jMdjSZKi236/j/KyrFp97E/TtMVi0Wg00goE77r1RymdzWaiKCqK0ul08vn4qxWyKPyh67ogCNFipVJZr9chZB4J775/+r5/PB4nk4mu64QQ27ZrtVpK+wpe8tDf1W63UxSl2+1alsU+E7zu+fzXbrcHg8HhcGAbBt6WOL83m81CocAyCnwgsT/XdWVZZhkFPnDrb7/fe553vTVNczQa3T/q+36v15vP5+zSwZ+iYyillBAiSZJhGJvNZjgcLpfL2FHVcRxBEFRVZXxEhiSr1d38cDqdttttEAT1er3VahWLxd9lU0rL5TIhhO0eg0TP5wfgBf4f8Q398Q398Q398e0bd3e/PHrW8vAAAAAASUVORK5CYII=",
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACIAAAAZCAIAAADbmGv7AAAACXBIWXMAAA7EAAAOxAGVKw4bAAABX0lEQVR4nO2VIc+CQBzGT2EUGAEJjI1EhQ9BMWEwmKCyGQh8ATc2PwojEExOC7MwgzOpgTkoBoOOhE0c3Bvc0InhYO/7BueTuP89z37c3Z+jBSEEf6/2PzC+mC8GALyW+3g82rZdDi3LkiQJJdiq9d0YhuH7/v2ZZdnVaoXjSC9aYzVxHGdZdjgc0COlapzNaDSiKGq9XjfAAIim7XZbRiRJWi6XiMG7UDFFUSRJEgSBaZoEQWAYNp/Pfx/zrM1m0+l0eJ7P8xwx8ui0yWRyvV7fbixN06qqPldc19V1fbfbybKMcjSPTmMY5na7vTWRJPlS6ff7AIB2G7mDGmwahPB8PguCUBQFoh8VE4ZhFEXlcDgcLhaLF89+v+/1emEYNsd0u10MwzRNG4/Hg8FgNptVPZ7nAQAcx6lOoV42l8tlOp2maSqKoqIoBEG8tZ1OJ47jqvV6d1pjfdb/5rMwP9l0bz4brisKAAAAAElFTkSuQmCC"
    ]
  },
  "explain_list": {},
  "correct_answers": [
    "blank"
  ]
}
```