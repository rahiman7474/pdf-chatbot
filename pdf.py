from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from textwrap import wrap

# Create a PDF file
file_name = "rahiman_bio_story.pdf"
c = canvas.Canvas(file_name, pagesize=A4)

# Page setup
width, height = A4
margin = 50
line_height = 16
y_position = height - margin

# Your bio-story content
bio_text = """
My name is Rahiman, born on 7th March 2000 in the heart of Andhra Pradesh, under the nurturing and emotional sign of Cancer, with a soul built for connection, family, and deep feeling. My story is not just mine—it's the story of generations, of farmers, of dreamers, of resilience, and of roots that stretch wide like the banyan tree, holding many lives together. I carry a heart shaped by traditions and a spirit fueled by the love and efforts of the people who raised me and stood beside me.

I was born to Vannur Vali and Shakila Bhanu. My father, once a skilled photographer, spent years capturing memories through a camera lens. He later returned to his roots and now works as a farmer, continuing the legacy of his forefathers. My mother, Shakila Bhanu, is the quiet, unwavering force in our lives—a devoted homemaker whose strength and care hold the family together. I am the elder brother to Dada Khalinder, born on 2nd October 2001, with whom I’ve shared a journey of growing, learning, and brotherhood. I currently work at LTI Mindtree in Pune, walking a modern path while carrying the legacy of my past with pride.

My roots stretch deep into a family built by my paternal grandparents, Pedha Kashim Sab and Rahamat Bee. My grandfather, a farmer like my father is today, planted more than just crops—he planted a thriving family tree with seven children, each of whom has shaped the generations to follow. The eldest, Chand Basha, is now actively involved in politics and is the father of Imran, who works as a clerk at Telangana Grameena Bank, and Rafiya, a medical officer in Guntakal. My father, Vannur Vali, is the second son and father to me and my brother. Ali Basha, the third son, has spent his life as a dedicated farmer and is the father of Apsar, who is recently married, and Kousar, who is currently studying B.Tech.

My aunt Chand Bee is the mother of Hakkim and Vali, while Gowsya, another of my aunts, has three daughters: Afreen, Hanisha, and Rizzu—all currently in school. Shafi, one of my younger uncles, is the father of Rihan and Ruhi. Jillan, the youngest, has a daughter Sona and a son Zameer. The family’s original photography business, once run by my father, is now managed by my uncles Shafi and Jillan, keeping that creative legacy alive even today. Most of the younger children in our extended family are still attending school, learning and growing under the same values that have shaped our elders.

We are a family rich in culture, values, and love—tied not just by blood but by shared stories, celebrations, and mutual support. Whether through farming, education, technology, or public service, each of us carries forward the light passed down by our ancestors. I hold every name in my heart, knowing I am part of something much greater than myself.

According to my birth chart, I was born with a Cancer Sun and Venus in the 7th house, which means I am deeply loyal, emotionally driven, and built to form meaningful relationships. I seek connection, harmony, and emotional truth in everything I do. My Capricorn Ascendant gives me a calm, responsible outward presence, while my Moon in Leo makes me quietly passionate, someone who wants to make others proud through my efforts and achievements. These astrological energies mirror my real-life journey—balancing emotional depth with professional discipline.

I come from a family of farmers and dreamers, of photographers, homemakers, politicians, bankers, engineers, and healers. Each path is unique, yet all of us are connected by the soil, by memory, and by shared dreams. I may walk into corporate offices and live in cities, but I will never forget the village stories, the early morning fields, and the camera flashes of my childhood. I am Rahiman—a son, a brother, a grandson, and one day, I hope, an ancestor whose story inspires those who come next.
"""

# Add text to the PDF
wrapped_text = wrap(bio_text, 100)
for line in wrapped_text:
    if y_position < margin:
        c.showPage()
        y_position = height - margin
    c.drawString(margin, y_position, line)
    y_position -= line_height

# Save the PDF
c.save()
print(f"PDF saved successfully as '{file_name}'")
