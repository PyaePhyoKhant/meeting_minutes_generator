import openai
import textwrap


openai.api_key = "your_openai_api_key"

def audio_to_text(audio_path):
    audio_file = open(audio_path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript

def call_chat_completion(system_prompt, user_prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    return response

def transcript_to_meeting_minutes(meeting_text, chunk_size=10000):
    """
    Generate meeting minutes from a meeting transcript using an iterative approach.
    
    This function breaks the transcript into chunks, creates meeting minutes from the first chunk,
    and then iteratively modifies the meeting minutes based on the subsequent chunks.
    
    Args:
        meeting_text (str): The meeting transcript text.
        chunk_size (int, optional): The size of the chunks the transcript is broken into. Defaults to 10000.

    Returns:
        str: The generated meeting minutes.
    """
    # Split the meeting text into chunks
    meeting_chunks = textwrap.wrap(meeting_text, chunk_size)

    # normal call to gpt for first chunk
    first_chunk = meeting_chunks[0]
    system_prompt = "You are an AI that generates meeting minutes from given meeting text."
    user_prompt = f"""Please generate meeting minutes from the following meeting text:\n\n{first_chunk}\n\n
    The meeting minutes should include the following sections:\n- Agenda\n- Attendees\n- Key Points\n- Decisions\n- Action Items
    """
    response = call_chat_completion(system_prompt, user_prompt)
    meeting_minutes = response['choices'][0]['message']['content']

    # call with another prompt with instruction to modify meeting minutes according to new chunk. notice different prompts
    system_prompt = "You are an AI that updates meeting minutes based on additional chunks of a meeting transcript."
    for chunk in meeting_chunks[1:]:
        user_prompt = f"""Here are the current meeting minutes:\n\n{meeting_minutes}\n\n
        Please update the meeting minutes based on the following chunk of the meeting transcript:\n\n{chunk}\n\n
        The meeting minutes should include these sections:\n- Agenda\n- Attendees\n- Key Points\n- Decisions\n- Action Items
        """
        response = call_chat_completion(system_prompt, user_prompt)
        meeting_minutes = response['choices'][0]['message']['content']

    return meeting_minutes
