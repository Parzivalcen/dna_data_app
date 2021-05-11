import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

#################
#PAGE TITLE
################

image = Image.open('dna.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleatide composition of query DNA!
""")

###########
# Input text box
###########

st.header('Enter Dna sequence')

sequence_input = "Example of a DNA sequence \n >DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area('Sequence input', sequence_input, height=250)

sequence = sequence.splitlines()
sequence = sequence[2:]

sequence = ''.join(sequence)

st.write("""
***
""")
st.header('INPUT(DNA QUERY)')
st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

x = DNA_nucleotide_count(sequence)
x

# Print text
st.subheader('2. Print text')
st.write('There are', str(x['A']), 'adenine (A)')
st.write('There are', str(x['T']), 'thymine (T)')
st.write('There are', str(x['G']), 'guanine (G)')
st.write('There are', str(x['C']), 'cytosine (C)')

# Display DataFrame
st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(x,orient='index')
df = df.rename({0:'count'}, axis=1)
df.reset_index(inplace=True)
df.rename(columns={'index':'Nucleotide'}, inplace=True)
st.write(df)

# Display bar chart
st.subheader('4. Display chart using Altair')
p = alt.Chart(df).mark_bar().encode(
    x='Nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)