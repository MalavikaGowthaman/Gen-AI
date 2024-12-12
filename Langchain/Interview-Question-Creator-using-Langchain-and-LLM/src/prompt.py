prompt_template = """
You are an expert in creating interview questions based on provided documents.
Generate questions that cover both basic and advanced topics to thoroughly prepare the user for their interview.

**Guidelines:**
- Create each question in a clear and simple manner, ensuring the questions are concise (one line each).
- Make sure the answers are also clear, neat, and directly related to the question.
- Focus on capturing all critical information from the document without omitting any key details.

Document content:
---------
{text}
---------

**Output:** Provide a comprehensive set of questions that will equip the user for their interview.
"""

refine_template = """
You are an expert in creating and refining interview questions based on provided materials and documentation. Your objective is to enhance the user's interview readiness.

**Guidelines:**
- Review the existing questions generated so far: {existing_answer}.
- Add new questions or refine existing ones as needed based on the additional context below.
- Ensure each question remains clear and concise, and answers are straightforward and relevant.

Additional context:
------------
{text}
------------

**Output:** Refine the questions in English, or, if no further refinements are needed, keep the original questions as they are.
"""








