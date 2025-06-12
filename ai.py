import gradio as gr
import difflib

# Predefined Q&A data
faq_data = [
    {
        "question": "What does the eligibility verification agent (EVA) do?",
        "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    },
    {
        "question": "What does the claims processing agent (CAM) do?",
        "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    },
    {
        "question": "How does the payment posting agent (PHIL) work?",
        "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
    },
    {
        "question": "Tell me about Thoughtful AI's Agents.",
        "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
    },
    {
        "question": "What are the benefits of using Thoughtful AI's agents?",
        "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
    }
]

# Fallback response for unknown questions
fallback_response = "I'm sorry, I couldn't find a specific answer to that. Please reach out to our support team for more information."

def get_answer(user_input):
    # Get list of all known questions
    questions = [item["question"] for item in faq_data]

    # Find the closest matching question (case-insensitive)
    closest_matches = difflib.get_close_matches(user_input.lower(), [q.lower() for q in questions], n=1, cutoff=0.5)

    if closest_matches:
        # Find original casing of the matched question
        matched_question = next(q for q in questions if q.lower() == closest_matches[0])
        # Find the corresponding answer
        for item in faq_data:
            if item["question"] == matched_question:
                return item["answer"]
    else:
        return fallback_response

# Set up Gradio interface
chat = gr.ChatInterface(fn=get_answer, title="Thoughtful AI Agent", chatbot=gr.Chatbot())

# Launch app
if __name__ == "__main__":
    chat.launch()
