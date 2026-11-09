# 1° Medio (A1) — Gramática, parte B
TEMAS = [
# ------------------------------------------------------------------ PERSONAL PRONOUNS
dict(slug="personal-pronouns", titulo="Personal Pronouns", nivel="1°", cefr="A1",
 objetivo="usar los pronombres personales sujeto (I, you, he, she, it, we, they) antes del verbo.",
 goal="use subject pronouns to replace names and nouns.",
 recordar=[
  "<b>I</b> (yo) · <b>you</b> (tú / usted) · <b>he</b> (él) · <b>she</b> (ella) · <b>it</b> (cosa / animal) · <b>we</b> (nosotros) · <b>you</b> (ustedes) · <b>they</b> (ellos/as)",
  "El pronombre va <b>antes del verbo</b> y en inglés <b>nunca se omite</b>: <i>She is my friend.</i> (no: <i>Is my friend.</i>)",
  "<b>I</b> siempre se escribe con mayúscula. Para animales y objetos usamos <b>it</b> (singular) y <b>they</b> (plural).",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Replace the words with a pronoun", instr="Escribe el pronombre que reemplaza a las palabras.", items=[
   "Pedro → [he]", "my sister → [she]", "the ship → [it]", "Ana and I → [we]", "the students → [they]", "my dog → [it]",
   "you and Tomás → [you]", "my parents → [they]", "Mrs. Rojas → [she]", "the books → [they]", "Mr. Soto → [he]", "my friends and I → [we]"]),
  dict(tipo="fill", titulo="Complete with the correct pronoun", instr="Completa con el pronombre sujeto adecuado.", items=[
   "This is Carla. [She] is my cousin.", "Look at the boat! [It] is beautiful.", "Diego and Luis are here. [They] are hungry.",
   "My name is Ana. [I] am fifteen.", "Mr. Pérez is a captain. [He] works on a ship.", "Javier and I are friends. [We] play football.",
   "The cats are black. [They] are cute.", "The weather is nice today. [It] is sunny.", "Where is my phone? [It] is on the table.",
   "Hi, Martina! Are [you] OK?"]),
  dict(tipo="choice", titulo="Choose the correct pronoun", instr="Encierra el pronombre correcto.", items=[
   "My mother is a nurse. {He|She*|It} works at a hospital.", "The computer is new. {It*|They|He} is fast.",
   "Tom and I are in 1° Medio. {They|We*|You} are classmates.", "My grandparents live in Viña. {We|They*|She} are nice.",
   "{I*|Me} am from Valparaíso.", "Sofía, {she|you*|they} are my best friend!",
   "The port is busy. {He|It*|They} has many ships.", "Carlos is tall. {He*|She|It} plays basketball."]),
  dict(tipo="rewrite", titulo="Rewrite with pronouns", instr="Reemplaza las palabras subrayadas (en negrita) por un pronombre.", cols=2, items=[
   "<b>Luis</b> is a student. => He is a student.", "<b>The ship</b> is big. => It is big.", "<b>My friends</b> are funny. => They are funny.",
   "<b>Paula and I</b> are tired. => We are tired.", "<b>The teacher</b> (woman) is kind. => She is kind.", "<b>The dogs</b> are hungry. => They are hungry.",
   "<b>My father</b> is a fisherman. => He is a fisherman.", "<b>The sea</b> is cold. => It is cold."]),
  dict(tipo="classify", titulo="Classify the words", instr="Clasifica cada palabra según el pronombre que la reemplaza.", categorias={
   "HE": ["my uncle", "the captain (man)", "Mr. Díaz"], "SHE": ["my aunt", "Camila", "the nurse (woman)"],
   "IT": ["the boat", "the city", "my phone"], "THEY": ["the students", "my shoes", "Ana and Leo"]}),
  dict(tipo="text", titulo="Complete the text", instr="Completa con I, you, he, she, it, we o they.", texto=
   "Hi! [I] am Benjamín. This is my family. My father is Jorge. [He] is a sailor. My mother is Paola. [She] is a teacher. "
   "I have two sisters. [They] are twins. We have a cat. [It] is white and very lazy. My family and I live in Valparaíso. "
   "[We] love our city. What about your family? Are [you] from Valparaíso too?"),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error en cada oración.", cols=2, items=[
   "i am a student. => I am a student.", "Is my brother. => He is my brother.", "My mom she is a cook. => My mom is a cook.",
   "The car, he is red. => The car is red.", "Me am fifteen. => I am fifteen.", "Is raining. => It is raining."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "She is my English teacher.", "They are from Argentina.", "It is a big port.", "We are in the same class.", "He works in Valparaíso."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee el texto y responde.", titulo_texto="The Rojas family", texto=
   "The Rojas family lives near the sea. Mr. Rojas is a fisherman. He goes to sea every morning. Mrs. Rojas is a cook. "
   "She works in a restaurant. They have two children, Elena and Tomás. They are students at the Instituto Marítimo. "
   "Elena likes engines and Tomás likes cooking. They have a dog. It is brown and it is called Rocky.",
   vf=[("Mr. Rojas is a cook.", False), ("Mrs. Rojas works in a restaurant.", True), ("Elena and Tomás are students.", True), ("The dog is black.", False)],
   preguntas=["What does Mr. Rojas do? => He is a fisherman.", "What does Elena like? => She likes engines.", "What is the dog's name? => It is called Rocky."]),
  dict(tipo="write", titulo="Describe people you know", instr="Escribe una oración sobre cada persona usando un pronombre.", items=[
   "My best friend:", "My mother / father:", "My classmates:", "My pet / my phone:"], modelo="My uncle: He is a mechanic. He is very funny."),
 ]),

# ------------------------------------------------------------------ POSSESSIVE ADJECTIVES
dict(slug="possessive-adjectives", titulo="Possessive Adjectives", nivel="1°", cefr="A1",
 objetivo="usar my, your, his, her, its, our, their para indicar pertenencia.",
 goal="use possessive adjectives to say who something belongs to.",
 recordar=[
  "I → <b>my</b> · you → <b>your</b> · he → <b>his</b> · she → <b>her</b> · it → <b>its</b> · we → <b>our</b> · they → <b>their</b>",
  "Van <b>antes del sustantivo</b> y no cambian en plural: <i>my book → my books</i>.",
  "Cuidado: <b>its</b> (posesivo) no es igual a <b>it's</b> (it is) · <b>their</b> (posesivo) no es igual a <b>they're</b> (they are).",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Match the pronoun and the possessive", instr="Escribe el adjetivo posesivo.", items=[
   "I → [my]", "you → [your]", "he → [his]", "she → [her]", "it → [its]", "we → [our]", "they → [their]"]),
  dict(tipo="fill", titulo="Complete with a possessive adjective", instr="Completa según el sujeto.", items=[
   "I have a cat. [My] cat is white.", "She has a bike. [Her] bike is blue.", "He has a sister. [His] sister is ten.",
   "We have a teacher. [Our] teacher is nice.", "They have a boat. [Their] boat is old.", "You have a phone. Is [your] phone new?",
   "The dog has a ball. [Its] ball is red.", "Tomás loves [his] school.", "Ana and Pedro visit [their] grandparents.",
   "My sister and I clean [our] room.", "The ship has [its] own crew.", "Camila does [her] homework."]),
  dict(tipo="choice", titulo="Choose the correct word", instr="Encierra la opción correcta.", items=[
   "This is {my*|I} pencil.", "{He|His*} name is Martín.", "{They|Their*} house is big.", "Is this {you|your*} bag?",
   "{Our*|We} school is in Valparaíso.", "The cat is eating {it's|its*} food.", "{Their|They're*} my friends.",
   "{Her*|She} eyes are green.", "{It's*|Its} a nice day.", "We love {our*|us} city."]),
  dict(tipo="rewrite", titulo="Rewrite with a possessive adjective", instr="Reemplaza las palabras en negrita.", cols=2, items=[
   "<b>Ana's</b> mother is a doctor. => Her mother is a doctor.", "<b>Pedro's</b> car is red. => His car is red.",
   "<b>My parents'</b> house is big. => Their house is big.", "<b>The dog's</b> name is Max. => Its name is Max.",
   "<b>Juan and Pedro's</b> dog is old. => Their dog is old.", "<b>Lucía's</b> phone is new. => Her phone is new."]),
  dict(tipo="text", titulo="Complete the text", instr="Completa con my, your, his, her, its, our o their.", texto=
   "Hello! [My] name is Florencia. I live with [my] family in Cerro Alegre. [My] father is Andrés. [His] job is on a ship. "
   "[My] mother is Teresa. [Her] job is in a bank. I have two brothers. [Their] names are Lucas and Mateo. "
   "We have a parrot. [Its] name is Pepe. [Our] house is small but colourful. What is [your] house like?"),
  dict(tipo="match", titulo="Match the halves", instr="Une las dos partes de cada oración.", pares=[
   ("I love", "my mother's food."), ("She brushes", "her teeth every morning."), ("They wash", "their car on Sundays."),
   ("He forgets", "his keys every day."), ("We clean", "our classroom on Fridays."), ("The bird opens", "its wings.")]),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error.", cols=2, items=[
   "She loves his mother. (Ana) => She loves her mother.", "They are doing they homework. => They are doing their homework.",
   "I like you bag. => I like your bag.", "The dog wags it's tail. => The dog wags its tail.",
   "We visit we grandma. => We visit our grandma.", "He name is Juan. => His name is Juan."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "Her brother is a sailor.", "Our teacher is very kind.", "Their house is near the port.", "What is your favourite colour?", "My dog loves its toys."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="My friend Joaquín", texto=
   "Joaquín is my best friend. His family is from Chiloé. His father is a fisherman and his mother is a teacher. "
   "Their house is next to the sea. Joaquín has a sister. Her name is Antonia and her hobby is painting. "
   "They also have a dog. Its name is Lobo. Our favourite activity is fishing with his father on Saturdays.",
   vf=[("Joaquín's family is from Chiloé.", True), ("His mother is a fisherwoman.", False), ("Antonia's hobby is painting.", True), ("The dog's name is Rocky.", False)],
   preguntas=["Where is their house? => It is next to the sea.", "What is their favourite activity? => Fishing with his father on Saturdays."]),
  dict(tipo="write", titulo="Write about your family and things", instr="Completa con información personal.", items=[
   "My favourite thing is", "My mother's / father's name is … His / Her job is", "Our house is", "My friends' names are … Their favourite"]),
 ]),

# ------------------------------------------------------------------ HAVE / HAS
dict(slug="have-has", titulo="Have / Has (posesión)", nivel="1°", cefr="A1",
 objetivo="usar el verbo have / has para describir posesiones en oraciones afirmativas, negativas e interrogativas.",
 goal="use have / has to talk about possessions in affirmative, negative and question forms.",
 recordar=[
  "<b>Afirmativo:</b> I / You / We / They → <b>have</b>  |  He / She / It → <b>has</b>",
  "<b>Negativo:</b> I / You / We / They → <b>don't have</b>  |  He / She / It → <b>doesn't have</b>",
  "<b>Preguntas:</b> <b>Do</b> I / you / we / they have…?  |  <b>Does</b> he / she / it have…?",
  "Respuestas cortas: Yes, I do. / No, I don't. · Yes, she does. / No, she doesn't.",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Complete with HAVE or HAS", instr="Completa cada oración con have o has según el sujeto.", items=[
   "My mother [has] a new job.", "I [have] two cats at home.", "We [have] English class today.", "He [has] a black bicycle.",
   "My friends [have] a football team.", "She [has] long curly hair.", "You [have] a nice smile.", "The dog [has] big brown eyes.",
   "My parents [have] a small shop.", "My little brother [has] many toys.", "Our classroom [has] new chairs.", "My sister and I [have] the same phone."]),
  dict(tipo="fill", titulo="Complete in the NEGATIVE form", instr="Completa con don't have o doesn't have.", largo=True, items=[
   "I [don't have] a car.", "She [doesn't have] a brother.", "They [don't have] homework today.", "My father [doesn't have] free time.",
   "We [don't have] a big house.", "He [doesn't have] a pet.", "You [don't have] my number.", "The school [doesn't have] a pool."]),
  dict(tipo="fill", titulo="Complete the questions with DO or DOES", instr="Completa con Do o Does y responde brevemente.", cols=1, items=[
   "[Do] you have a pen? — Yes, I [do].", "[Does] she have a sister? — No, she [doesn't].", "[Do] they have a car? — Yes, they [do].",
   "[Does] he have blue eyes? — No, he [doesn't].", "[Do] we have a test today? — Yes, we [do].", "[Does] the ship have a big crew? — Yes, it [does]."]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la forma correcta.", items=[
   "My uncle {have|has*} a boat.", "We {don't*|doesn't} have Wi-Fi at home.", "{Do|Does*} your mother have a car?",
   "Carlos {don't|doesn't*} have a computer.", "They {have*|has} three children.", "{Do*|Does} you have any brothers?",
   "It {have|has*} four legs.", "She doesn't {has|have*} a pet."]),
  dict(tipo="text", titulo="Complete the text", instr="Completa con have / has / don't have / doesn't have.", texto=
   "Hi! My name is Ana. I [have] a big family. My father [has] a red car and my mother [has] a small shop. "
   "I [have] two brothers, but I [don't have] a sister. My brother Pablo [has] a guitar, but he [doesn't have] a piano. "
   "We [have] a dog called Toby. Toby [has] a big house in the garden. My grandparents [don't have] a pet, but they [have] a beautiful garden."),
  dict(tipo="rewrite", titulo="Make negative sentences", instr="Escribe la oración en negativo.", cols=2, items=[
   "I have a bike. => I don't have a bike.", "She has a cat. => She doesn't have a cat.", "We have a big TV. => We don't have a big TV.",
   "He has a job. => He doesn't have a job.", "They have money. => They don't have money.", "The port has a museum. => The port doesn't have a museum."]),
  dict(tipo="rewrite", titulo="Write questions", instr="Escribe la pregunta con Do / Does.", cols=2, items=[
   "you / a laptop => Do you have a laptop?", "she / a boyfriend => Does she have a boyfriend?", "they / a garden => Do they have a garden?",
   "he / a passport => Does he have a passport?", "your school / a gym => Does your school have a gym?", "we / homework => Do we have homework?"]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My cousin has a new phone.", "We don't have class on Saturday.", "Does your father have a boat?", "They have two dogs and a cat.", "She doesn't have black hair."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee el texto y responde.", titulo_texto="Matías and his things", texto=
   "Matías is sixteen. He has a small room with a bed, a desk and a computer. He doesn't have a TV in his room, but he has a big poster of a ship. "
   "Matías has two hobbies: music and fishing. He has a guitar and a fishing rod. His best friend, Raúl, doesn't have a guitar, so they play Matías's guitar together. "
   "Matías and his family don't have a car. They have bicycles.",
   vf=[("Matías has a TV in his room.", False), ("He has a poster of a ship.", True), ("Raúl has a guitar.", False), ("The family has bicycles.", True)],
   preguntas=["What does Matías have in his room? => He has a bed, a desk and a computer.", "What are his hobbies? => Music and fishing.",
              "Does the family have a car? => No, they don't."]),
  dict(tipo="write", titulo="Write about you", instr="Escribe oraciones con have / has / don't have / doesn't have.", items=[
   "I have", "I don't have", "My best friend has", "My family doesn't have"]),
 ]),

# ------------------------------------------------------------------ ARTICLES
dict(slug="articles", titulo="Articles: a / an / the", nivel="1°", cefr="A1",
 objetivo="usar correctamente los artículos a, an y the.",
 goal="use the articles a, an and the correctly.",
 recordar=[
  "<b>a</b> + sonido consonante: <i>a ship, a university, a big egg</i>  ·  <b>an</b> + sonido vocal: <i>an apple, an hour, an engineer</i>",
  "<b>a / an</b> = uno, algo no específico o que se menciona por primera vez: <i>I have a dog.</i>",
  "<b>the</b> = algo específico o ya mencionado, o único: <i>The dog is black. The sun, the sea, the Pacific Ocean.</i>",
  "Sin artículo: plurales y cosas en general: <i>I like dogs.</i>  Profesiones llevan a/an: <i>She is a nurse.</i>",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Write A or AN", instr="Escribe a o an.", items=[
   "[a] boat", "[an] anchor", "[an] engine", "[a] captain", "[an] island", "[an] orange", "[a] uniform", "[an] hour",
   "[a] map", "[an] umbrella", "[a] house", "[an] old ship"]),
  dict(tipo="fill", titulo="Complete with a / an / the", instr="Completa con el artículo correcto.", items=[
   "I have [a] cat. [The] cat is grey.", "She is [an] engineer.", "[The] sun is very hot today.", "Can you open [the] door, please?",
   "There is [an] apple on the table.", "My father is [a] mechanic.", "[The] Pacific Ocean is very big.", "I want [an] ice cream."]),
  dict(tipo="choice", titulo="Choose the correct article", instr="Encierra la opción correcta (– = sin artículo).", items=[
   "He is {a|an*} electrician.", "I love {the|–*} music.", "Look at {a|the*} moon!", "She has {a*|an} uniform.",
   "We go to school by {the|–*} bus.", "It's {a|an*} easy exercise.", "{The*|A} teacher in room 5 is nice.", "I eat {an*|a} egg every morning."]),
  dict(tipo="classify", titulo="A or AN?", instr="Clasifica las palabras según el artículo.", categorias={
   "A": ["ship", "sailor", "university", "radio", "key"], "AN": ["officer", "egg", "hour", "idea", "ocean"]}),
  dict(tipo="text", titulo="Complete the story", instr="Completa con a, an o the.", texto=
   "Yesterday I saw [a] ship and [an] old boat in the port. [The] ship was enormous and [the] boat was very small. "
   "On [the] ship there was [a] captain with [an] orange jacket. He had [a] map in his hand. [The] map showed [an] island in the south. "
   "I think [the] captain was going to [the] island."),
  dict(tipo="rewrite", titulo="Correct the mistakes", instr="Corrige el error del artículo.", cols=2, items=[
   "She is a engineer. => She is an engineer.", "I have an car. => I have a car.", "A sun is hot. => The sun is hot.",
   "He is teacher. => He is a teacher.", "I like the dogs. (in general) => I like dogs.", "It is a hour. => It is an hour."]),
  dict(tipo="match", titulo="Match the job and the definition", instr="Une la profesión con su definición.", pares=[
   ("a captain", "is the boss on a ship."), ("an engineer", "designs and repairs machines."), ("a cook", "prepares food."),
   ("an electrician", "works with cables and lights."), ("a nurse", "helps doctors in a hospital."), ("a fisherman", "catches fish in the sea.")]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My uncle is an engineer.", "The ship has an orange flag.", "I need a pen and an eraser.", "The sea is cold in winter."]),
  dict(tipo="choice", titulo="Article or no article?", instr="Encierra la opción correcta (– = sin artículo).", items=[
   "I play {the|–*} football on Saturdays.", "She plays {the*|–} guitar.", "{The|–*} cats are nice animals.", "We have {–*|the} lunch at one.",
   "{The*|–} Andes are very high.", "I go to {–*|the} school by bus.", "Can you pass me {the*|–} salt?", "My father is {–|a*} sailor."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="A day at the port", texto=
   "On Saturday, Laura went to the port with her father. They saw a ferry, a cargo ship and an old fishing boat. The ferry was white and the cargo ship was red. "
   "The fishing boat had an orange sail. They also met an officer from the navy. The officer showed them a map of the port. "
   "At the end of the day, they ate an empanada and drank a juice.",
   vf=[("Laura went to the port with her mother.", False), ("The ferry was white.", True), ("The fishing boat had an orange sail.", True), ("They met a teacher.", False)],
   preguntas=["What did the officer show them? => He showed them a map of the port.", "What did they eat? => They ate an empanada."]),
  dict(tipo="write", titulo="Your turn", instr="Escribe oraciones con a / an / the.", items=[
   "In my bag I have", "My dream job is", "In my classroom there is", "The best place in my city is"]),
 ]),
]
