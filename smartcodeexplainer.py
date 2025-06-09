{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e08f52a5-756b-4746-9971-ded7811aaf2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* Running on local URL:  http://127.0.0.1:7862\n",
      "* To create a public link, set `share=True` in `launch()`.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div><iframe src=\"http://127.0.0.1:7862/\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": []
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import gradio as gr\n",
    "import google.generativeai as genai\n",
    "\n",
    "genai.configure(api_key=\"AIzaSyAOQBR85UtpULED-HOs7dnpYFQXGc\")\n",
    "model = genai.GenerativeModel(\"gemini-1.5-flash\")\n",
    "\n",
    "def explain_code(code_input):\n",
    "    if not code_input.strip():\n",
    "        return \"Please enter some code to explain.\"\n",
    "    prompt = f\"Explain the following code in a clear and concise manner. Break down its functionality and purpose:\\n\\n```\\n{code_input}\\n```\"\n",
    "    try:\n",
    "        response = model.generate_content(prompt)\n",
    "        return response.text\n",
    "    except Exception as e:\n",
    "        return f\"An error occurred: {e}\"\n",
    "\n",
    "iface = gr.Interface(\n",
    "    fn=explain_code,\n",
    "    inputs=gr.Textbox(lines=15, label=\"Enter your code here:\", placeholder=\"Paste your code (Python, JavaScript, Java, etc.)\"),\n",
    "    outputs=gr.Textbox(lines=20, label=\"Code Explanation:\", placeholder=\"The explanation will appear here...\"),\n",
    "    title=\"Smart Code Explainer\",\n",
    "    description=\"Paste your code into the input box, and I'll explain its functionality using Google Gemini AI. Supports various programming languages.\"\n",
    ")\n",
    "\n",
    "iface.launch()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "05faae71-e71c-46d3-bb30-4568e82472cc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
