def welcome_assignment_answers(question: str):
    questions = {
        "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?": "mtls",
        "Are encoding and encryption the same? - Yes/No": "No",
        "Is it possible to decrypt a message without a key? - Yes/No": "No",
        "Is it possible to decode a message without a key? - Yes/No": "No",
        "Is a hashed message supposed to be un-hashed? - Yes/No": "No",
        "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code": "8496abe9fceb5aa927e28bfbd9a2347d1290ef9b",
        "Is MD5 a secured hashing algorithm? - Yes/No": "No",
        "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number": 4,
        "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number": 3,

    }
    
    return questions.get(question, "Invalid question")
