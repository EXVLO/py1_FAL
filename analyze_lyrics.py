def analyze_lyrics(lyrics):
    never_gonna_count = lyrics.lower().count("never gonna")
    
    lines = lyrics.split('\n')
    cleaned_lines = [line for line in lines if not line.strip().startswith('[')]
    cleaned_lyrics = '\n'.join(cleaned_lines)
    
    line_count = len(cleaned_lines)
    
    alphabet_count = sum(1 for char in lyrics if char.isalpha())
    
    return {
        'never_gonna_count': never_gonna_count,
        'cleaned_lyrics': cleaned_lyrics,
        'line_count': line_count,
        'alphabet_count': alphabet_count
    }

lyrics = """[Intro]
Desert you
Ooh-ooh-ooh-ooh
Hurt you

[Verse 1]
We're no strangers to love
You know the rules and so do I (Do I)
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

[Pre-Chorus]
I just wanna tell you how I'm feeling
Gotta make you understand

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

[Verse 2]
We've known each other for so long
Your heart's been aching, but you're too shy to say it (To say it)
Inside, we both know what's been going on (Going on)
We know the game, and we're gonna play it

[Pre-Chorus]
And if you ask me how I'm feeling
Don't tell me you're too blind to see

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

[Bridge]
Ooh (Give you up)
Ooh-ooh (Give you up)
Ooh-ooh
Never gonna give, never gonna give (Give you up)
Ooh-ooh
Never gonna give, never gonna give (Give you up)
[Verse 3]
We've known each other for so long
Your heart's been aching, but you're too shy to say it (To say it)
Inside, we both know what's been going on (Going on)
We know the game, and we're gonna play it

[Pre-Chorus]
I just wanna tell you how I'm feeling
Gotta make you understand

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you"""

results = analyze_lyrics(lyrics)

print("=" * 50)
print("LYRICS ANALYSIS RESULTS")
print("=" * 50)

print(f"\n1. Number of 'never gonna'/'Never gonna': {results['never_gonna_count']}")

print(f"\n2. Lyrics without section separators:")
print("-" * 30)
print(results['cleaned_lyrics'])

print(f"\n3. Number of lines after removing section separators: {results['line_count']}")

print(f"\n4. Number of alphabets in the lyrics: {results['alphabet_count']}")

print("\n" + "=" * 50)