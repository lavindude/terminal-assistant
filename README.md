# Setup + Development

Create a .env file with necessary environment variables.

```bash
brew install portaudio
```

Create venv:

```bash
python3 -m venv .venv

source .venv/bin/activate
pip install -r requirements.txt
deactivate
```


When you add new libraries: pip freeze > requirements.txt

# Thoughts/challenges
- memory log will get stored as context and sent to bedrock, this could be very large
and cause lm delay
- conversation array could have the same issue
- use with headphones to avoid sound going into microphone (speech not waiting)
