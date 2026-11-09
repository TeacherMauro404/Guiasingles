# 1° Medio (A1) — Vocabulario y escritura
TEMAS = [
# ------------------------------------------------------------------ FAMILY
dict(slug="family", titulo="The Family", nivel="1°", cefr="A1",
 objetivo="nombrar a los miembros de la familia y describirlos con el verbo to be y have.",
 goal="name family members and describe them.",
 recordar=[
  "<b>parents</b> (padres): father / mother · <b>children</b>: son / daughter · <b>siblings</b>: brother / sister",
  "<b>grandparents</b>: grandfather / grandmother · <b>grandchildren</b>: grandson / granddaughter",
  "uncle (tío) · aunt (tía) · cousin (primo/a) · nephew (sobrino) · niece (sobrina) · husband (esposo) · wife (esposa)",
 ],
 ejercicios=[
  dict(tipo="match", titulo="Match the English and Spanish words", instr="Une la palabra con su traducción.", pares=[
   ("grandmother", "abuela"), ("uncle", "tío"), ("cousin", "primo / prima"), ("nephew", "sobrino"), ("niece", "sobrina"),
   ("husband", "esposo"), ("daughter", "hija"), ("siblings", "hermanos")]),
  dict(tipo="classify", titulo="Male, female or both?", instr="Clasifica las palabras.", categorias={
   "MALE": ["father", "son", "uncle", "nephew", "grandfather"], "FEMALE": ["mother", "daughter", "aunt", "niece", "wife"], "BOTH": ["cousin", "parents", "children", "siblings", "grandparents"]}),
  dict(tipo="fill", titulo="Complete the family relations", instr="Completa con la palabra correcta.", items=[
   "My mother's mother is my [grandmother].", "My father's brother is my [uncle].", "My aunt's son is my [cousin].", "My sister's son is my [nephew].",
   "My brother's daughter is my [niece].", "My mother's husband is my [father].", "My parents' parents are my [grandparents].", "My father's sister is my [aunt].",
   "My mother and father are my [parents].", "My grandmother's husband is my [grandfather]."]),
  dict(tipo="text", titulo="Read the family tree text and complete", instr="Completa el texto con palabras de familia.", banco=["wife", "son", "daughter", "brother", "grandparents", "cousins", "uncle", "aunt"], texto=
   "Hi, I'm Antonia. My father is Hugo and my mother is Rosa. Rosa is Hugo's [wife]. I have a [brother], Vicente. He is my parents' [son] and I'm their [daughter]. "
   "My father's brother is Tío Marcos; he is my [uncle]. His wife, Carmen, is my [aunt]. They have two children, Ema and Bruno. They are my [cousins]. "
   "On Sundays we all visit my [grandparents] in Limache."),
  dict(tipo="choice", titulo="Choose the correct word", instr="Encierra la opción correcta.", items=[
   "My uncle's daughter is my {cousin*|niece}.", "I am my grandmother's {grandson*|nephew}.", "My {wife|parents*} are Raúl and Inés.",
   "My sister's husband is my {brother-in-law*|uncle}.", "My {aunt*|uncle} is a nurse. She works at night.", "My brother and I are {siblings*|cousins}."]),
  dict(tipo="fill", titulo="Describe family members", instr="Completa con is / are / has / have.", items=[
   "My father [is] tall and strong.", "My grandparents [are] very kind.", "My sister [has] long hair.", "My cousins [have] a dog.",
   "My mother [is] a nurse.", "My uncle [has] a boat.", "We [are] a big family.", "My nephews [are] twins."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My grandmother is seventy years old.", "I have two cousins in Santiago.", "My father's name is Hugo.", "Do you have any brothers or sisters?"]),
  dict(tipo="rewrite", titulo="Answer about YOUR family", instr="Responde con oraciones completas.", cols=1, items=[
   "How many people are there in your family? => There are … people in my family.", "Do you have any brothers or sisters? => Yes, I have … / No, I don't.",
   "What is your mother's / father's name? => My mother's name is …", "Who is your favourite relative? Why? => My favourite relative is … because …"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="A family of sailors", texto=
   "Gonzalo is seventeen and he comes from a family of sailors. His grandfather, Don Pedro, was a captain for forty years. "
   "His father works on a cargo ship and his uncle is a fisherman in San Antonio. Gonzalo's mother is a nurse and his older sister, Fernanda, studies engineering. "
   "Gonzalo wants to be a ship's officer like his father. His family is very proud of him.",
   vf=[("Gonzalo's grandfather was a captain.", True), ("His uncle works on a cargo ship.", False), ("His sister studies engineering.", True), ("His mother is a teacher.", False)],
   preguntas=["Where does his uncle work? => In San Antonio, as a fisherman.", "What does Gonzalo want to be? => A ship's officer, like his father."]),
  dict(tipo="write", titulo="Write about your family", instr="Escribe un párrafo corto (5 oraciones) sobre tu familia.", items=[
   "In my family there are", "My mother / father is", "I have", "My favourite relative is", "We like"]),
 ]),

# ------------------------------------------------------------------ NUMBERS & DATES
dict(slug="numbers-dates", titulo="Numbers & Dates", nivel="1°", cefr="A1",
 objetivo="usar números cardinales y ordinales, días, meses y fechas.",
 goal="say and write numbers, days, months and dates.",
 recordar=[
  "Cardinales: 13 thirteen · 30 thirty · 15 fifteen · 50 fifty · 100 one hundred · 1,000 one thousand",
  "Ordinales: 1st first · 2nd second · 3rd third · 4th fourth · 5th fifth · 12th twelfth · 20th twentieth · 21st twenty-first",
  "Fechas: <i>on Monday, on 18th September</i> · <i>in May, in 2026</i>  ·  Se dice: <i>the eighteenth of September</i>",
  "Días: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday (¡siempre con mayúscula!)",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write the numbers in words", instr="Escribe el número en palabras.", items=[
   "12 → [twelve]", "15 → [fifteen]", "20 → [twenty]", "33 → [thirty-three]", "40 → [forty]", "58 → [fifty-eight]",
   "71 → [seventy-one]", "99 → [ninety-nine]", "100 → [one hundred]", "250 → [two hundred and fifty]"]),
  dict(tipo="fill", titulo="Ordinal numbers", instr="Escribe el ordinal en palabras.", items=[
   "1st → [first]", "2nd → [second]", "3rd → [third]", "5th → [fifth]", "8th → [eighth]", "9th → [ninth]", "12th → [twelfth]", "20th → [twentieth]",
   "21st → [twenty-first]", "30th → [thirtieth]"]),
  dict(tipo="fill", titulo="Days and months", instr="Completa la secuencia.", cols=1, items=[
   "Monday, [Tuesday], Wednesday, [Thursday], Friday, [Saturday], Sunday",
   "January, [February], March, [April], May, [June]", "July, [August], [September], October, [November], December"]),
  dict(tipo="choice", titulo="Thirteen or thirty?", instr="Encierra el número correcto.", items=[
   "13 = {thirteen*|thirty}", "50 = {fifteen|fifty*}", "14 = {fourteen*|forty}", "80 = {eighteen|eighty*}", "16 = {sixteen*|sixty}", "90 = {nineteen|ninety*}"]),
  dict(tipo="fill", titulo="Important dates in Chile", instr="Escribe la fecha en inglés (ordinal + month).", cols=1, largo=True, items=[
   "Christmas: [25th December / the twenty-fifth of December]", "National Holiday (Fiestas Patrias): [18th September / the eighteenth of September]",
   "New Year's Day: [1st January / the first of January]", "Día de las Glorias Navales: [21st May / the twenty-first of May]", "My birthday: [respuesta personal]"]),
  dict(tipo="fill", titulo="Prepositions with dates", instr="Completa con in, on o at.", items=[
   "My birthday is [in] March.", "We have English [on] Tuesday.", "The ship arrives [on] 3rd July.", "I was born [in] 2010.",
   "School starts [in] March.", "Class starts [at] 8 o'clock.", "We go to the beach [in] summer.", "The party is [on] Saturday."]),
  dict(tipo="fill", titulo="Maths in English", instr="Resuelve y escribe el resultado en palabras.", items=[
   "seven + eight = [fifteen]", "twenty - six = [fourteen]", "nine × three = [twenty-seven]", "forty ÷ two = [twenty]", "eleven + nineteen = [thirty]", "a hundred - one = [ninety-nine]"]),
  dict(tipo="text", titulo="Complete the text", instr="Escribe los números y fechas en palabras.", texto=
   "My name is Ignacio and I'm [fifteen] (15) years old. My birthday is on the [twelfth] (12th) of [August] (08). "
   "There are [thirty-two] (32) students in my class. Our school has [three] (3) workshops and [four] (4) labs. "
   "My favourite day is [Friday] because we have sport. The [first] (1st) day of school was in [March] (03)."),
  dict(tipo="fill", titulo="Say the years", instr="Escribe el año en palabras (ej. 1990 = nineteen ninety).", items=[
   "1810 → [eighteen ten]", "1879 → [eighteen seventy-nine]", "1990 → [nineteen ninety]", "2000 → [two thousand]", "2010 → [twenty ten / two thousand and ten]", "2026 → [twenty twenty-six]"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Ship schedule — Port of Valparaíso", texto=
   "Monday 3rd March: the cruise ship 'Aurora' arrives with 2,500 passengers. Wednesday 5th March: the cargo ship 'Andes' leaves for China. "
   "Friday 7th March: the navy ship 'Esmeralda' visits the port; tickets cost 3,000 pesos. Sunday 9th March: no ships.",
   vf=[("'Aurora' arrives on Monday.", True), ("'Andes' leaves on Thursday.", False), ("'Esmeralda' visits on the 7th.", True), ("There are ships on Sunday.", False)],
   preguntas=["How many passengers does 'Aurora' bring? => Two thousand five hundred.", "How much are the tickets for 'Esmeralda'? => Three thousand pesos."]),
  dict(tipo="write", titulo="About you", instr="Responde escribiendo los números en palabras.", items=[
   "My birthday is on", "My phone number is", "My favourite day of the week is", "My favourite month is … because"]),
 ]),

# ------------------------------------------------------------------ COLORS & CLASSROOM
dict(slug="colors-classroom", titulo="Colors & Classroom Objects", nivel="1°", cefr="A1",
 objetivo="nombrar colores y objetos de la sala de clases, y usar expresiones típicas de clase.",
 goal="name colours, classroom objects and use classroom language.",
 recordar=[
  "Colours: red, blue, yellow, green, orange, purple, pink, brown, black, white, grey, light / dark blue",
  "Objects: pen, pencil, eraser (rubber), ruler, pencil case, notebook, book, desk, chair, board, marker, scissors, glue, backpack",
  "El adjetivo va <b>antes</b> del sustantivo y no cambia en plural: <i>a red pen → two red pens</i>.",
  "Classroom language: <i>Can you repeat, please? · How do you say … in English? · May I go to the toilet? · I don't understand.</i>",
 ],
 ejercicios=[
  dict(tipo="match", titulo="Match the object and the translation", instr="Une cada palabra con su traducción.", pares=[
   ("eraser", "goma"), ("ruler", "regla"), ("pencil case", "estuche"), ("scissors", "tijeras"), ("glue", "pegamento"),
   ("board", "pizarra"), ("backpack", "mochila"), ("notebook", "cuaderno")]),
  dict(tipo="fill", titulo="Mix the colours", instr="Escribe el color resultante.", items=[
   "red + yellow = [orange]", "blue + yellow = [green]", "red + white = [pink]", "black + white = [grey]", "red + blue = [purple]", "blue + white = [light blue]"]),
  dict(tipo="fill", titulo="What colour is it?", instr="Escribe el color típico.", items=[
   "the sea → [blue]", "a banana → [yellow]", "grass → [green]", "the Chilean flag → [red, white and blue]", "snow → [white]", "chocolate → [brown]",
   "a tomato → [red]", "the night sky → [black / dark blue]"]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "I have a {red pen*|pen red}.", "These are {blues books|blue books*}.", "Can you {repeat*|repit}, please?", "How do you {say*|tell} 'goma' in English?",
   "I need {a*|an} ruler.", "She has {an*|a} orange backpack.", "{May*|Do} I go to the toilet?", "I don't {understand*|understood}."]),
  dict(tipo="classify", titulo="Classify the words", instr="Clasifica en colores y objetos.", categorias={
   "COLOURS": ["purple", "grey", "brown", "pink", "orange"], "OBJECTS": ["marker", "chair", "glue", "scissors", "ruler"]}),
  dict(tipo="match", titulo="Classroom language", instr="Une la frase en inglés con su significado.", pares=[
   ("Can you repeat, please?", "¿Puede repetir, por favor?"), ("I don't understand.", "No entiendo."), ("How do you spell it?", "¿Cómo se deletrea?"),
   ("Can I borrow your pen?", "¿Me prestas tu lápiz?"), ("What page?", "¿Qué página?"), ("Sorry I'm late.", "Disculpe la tardanza.")]),
  dict(tipo="text", titulo="Complete the dialogue", instr="Completa con palabras del recuadro.", banco=["borrow", "pencil case", "red", "eraser", "understand", "repeat"], texto=
   "TEACHER: Open your books on page 34.\nLUIS: Sorry, I don't [understand]. Can you [repeat], please?\nTEACHER: Page thirty-four.\n"
   "LUIS: Thanks. Martina, can I [borrow] your pen?\nMARTINA: Sure. Which one, the blue one or the [red] one?\nLUIS: The blue one. Do you have an [eraser] too?\n"
   "MARTINA: Yes, it's in my [pencil case]."),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My pencil case is purple and black.", "Can I borrow your ruler?", "There are two green markers on the desk.", "How do you say 'tijeras' in English?"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="What's in Javiera's backpack?", texto=
   "Javiera's backpack is dark blue. Inside, she has three notebooks: a red one for English, a green one for Maths and a yellow one for Science. "
   "Her pencil case is pink. In it there are two pencils, a black pen, an eraser, a small ruler and some coloured markers. "
   "She doesn't have scissors, so she always borrows them from her friend Simón.",
   vf=[("The backpack is light blue.", False), ("The English notebook is red.", True), ("The pencil case is pink.", True), ("She has scissors.", False)],
   preguntas=["What colour is the Science notebook? => It's yellow.", "Who lends her scissors? => Her friend Simón."]),
  dict(tipo="write", titulo="Describe your backpack and desk", instr="Escribe 4 oraciones con colores y objetos.", items=[
   "My backpack is", "In my pencil case there is / are", "On my desk there is", "My favourite colour is"]),
 ]),

# ------------------------------------------------------------------ COUNTRIES & NATIONALITIES
dict(slug="countries-nationalities", titulo="Countries & Nationalities", nivel="1°", cefr="A1",
 objetivo="nombrar países, nacionalidades e idiomas, y preguntar por el origen.",
 goal="talk about countries, nationalities and languages.",
 recordar=[
  "-an / -ian: Chile → Chilean, Peru → Peruvian, Argentina → Argentinian, Brazil → Brazilian, Italy → Italian, Mexico → Mexican",
  "-ish: England → English, Spain → Spanish · -ese: China → Chinese, Japan → Japanese · otras: France → French, Greece → Greek",
  "Nacionalidades e idiomas van con <b>mayúscula</b>: <i>She is Brazilian. She speaks Portuguese.</i>",
  "<i>Where are you from? — I'm from Chile. I'm Chilean.</i>",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write the nationality", instr="Escribe la nacionalidad.", items=[
   "Chile → [Chilean]", "Peru → [Peruvian]", "Argentina → [Argentinian]", "Brazil → [Brazilian]", "Spain → [Spanish]", "England → [English]",
   "China → [Chinese]", "Japan → [Japanese]", "France → [French]", "Germany → [German]", "Italy → [Italian]", "the USA → [American]"]),
  dict(tipo="classify", titulo="Classify by ending", instr="Clasifica las nacionalidades según su terminación.", categorias={
   "-AN / -IAN": ["Mexican", "Colombian", "Bolivian"], "-ISH": ["British", "Irish", "Turkish"], "-ESE": ["Portuguese", "Vietnamese", "Chinese"], "OTHER": ["French", "Greek", "Dutch"]}),
  dict(tipo="fill", titulo="What language do they speak?", instr="Escribe el idioma.", items=[
   "In Brazil they speak [Portuguese].", "In France they speak [French].", "In Japan they speak [Japanese].", "In Chile they speak [Spanish].",
   "In Germany they speak [German].", "In Australia they speak [English].", "In China they speak [Chinese / Mandarin].", "In Italy they speak [Italian]."]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "I'm from {Chile*|Chilean}.", "She is {Peru|Peruvian*}.", "They speak {english|English*}.", "Is he {Mexico|Mexican*}?",
   "We are {chileans|Chilean*}.", "My teacher is from the {UK*|British}.", "Pizza is {Italian*|Italy} food.", "Where {are*|is} you from?"]),
  dict(tipo="rewrite", titulo="Write sentences", instr="Escribe una oración como el ejemplo.", cols=1, items=[
   "Hiro / Japan => Hiro is from Japan. He is Japanese. He speaks Japanese.", "Ana / Brazil => Ana is from Brazil. She is Brazilian. She speaks Portuguese.",
   "Pierre and Claire / France => They are from France. They are French. They speak French.", "Carlos / Mexico => Carlos is from Mexico. He is Mexican. He speaks Spanish."]),
  dict(tipo="text", titulo="Complete the text", instr="Completa con países, nacionalidades o idiomas.", texto=
   "Many ships from different countries arrive in Valparaíso. Today there is a ship from China. The crew is [Chinese] and they speak Chinese. "
   "There is also a ship from Panama; the captain is [Panamanian]. A cruise ship has tourists from the United States — they are [American] and they speak [English]. "
   "A Brazilian sailor speaks [Portuguese], but he understands Spanish. I'm from [Chile], so I'm Chilean, and I want to speak many languages!"),
  dict(tipo="match", titulo="Match the famous thing and the country", instr="Une con el país.", pares=[
   ("The Eiffel Tower", "France"), ("Machu Picchu", "Peru"), ("The Great Wall", "China"), ("Easter Island (Rapa Nui)", "Chile"),
   ("The Colosseum", "Italy"), ("Big Ben", "England")]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "Where are you from?", "My grandfather is Italian.", "They speak Portuguese in Brazil.", "Is your teacher American?"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="An international crew", texto=
   "The cargo ship 'Southern Star' has an international crew. The captain, Mr. Lindqvist, is Swedish. The chief engineer is from the Philippines; he is Filipino. "
   "There are three Chilean officers and two cooks from Peru. On the ship, they all speak English, because it is the international language of the sea. "
   "At dinner, the Peruvian cooks prepare ceviche and everybody loves it.",
   vf=[("The captain is from Sweden.", True), ("The chief engineer is Chilean.", False), ("The crew speaks English on the ship.", True), ("The cooks are Brazilian.", False)],
   preguntas=["Why do they speak English? => Because it is the international language of the sea.", "What do the cooks prepare? => Ceviche."]),
  dict(tipo="write", titulo="Your turn", instr="Escribe sobre ti y un país que te gustaría visitar.", items=[
   "I'm from … I'm", "I speak", "I want to visit … because", "People there are … and they speak"]),
 ]),
]
