import os,sys
GROQ_API_KEY=os.environ.get('GROQ_API_KEY','')
def main():
    print(f"GROQ: {'OK' if GROQ_API_KEY else 'MISSING'}")
if __name__ == '__main__':
    main()
