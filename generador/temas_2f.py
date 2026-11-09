# 2° Medio (A2) — Vocabulario, parte A
TEMAS = [
# ------------------------------------------------------------------ FEELINGS
dict(slug="feelings", titulo="Feelings & Moods", nivel="2°", cefr="A2",
 objetivo="expresar sentimientos y estados de ánimo, y explicar sus causas.",
 goal="talk about feelings and explain why you feel that way.",
 recordar=[
  "Positivos: happy, excited, proud, relaxed, calm, surprised · Negativos: sad, angry, worried, nervous, scared, bored, tired, lonely, embarrassed",
  "<b>to be + adjetivo</b>: <i>I'm nervous. She is worried.</i> · <b>feel + adjetivo</b>: <i>I feel tired.</i>",
  "Causa: <i>I'm happy <b>because</b> it's Friday.</i> · <b>-ed</b> (cómo me siento) vs <b>-ing</b> (cómo es algo): <i>I'm bored. The film is boring.</i>",
 ],
 ejercicios=[
  dict(tipo="match", titulo="Match the feeling and the translation", instr="Une cada adjetivo con su significado.", pares=[
   ("worried", "preocupado"), ("proud", "orgulloso"), ("scared", "asustado"), ("bored", "aburrido"), ("embarrassed", "avergonzado"),
   ("lonely", "solo / solitario"), ("excited", "entusiasmado"), ("angry", "enojado")]),
  dict(tipo="classify", titulo="Positive or negative?", instr="Clasifica los sentimientos.", categorias={
   "POSITIVE": ["happy", "relaxed", "proud", "excited", "calm"], "NEGATIVE": ["nervous", "lonely", "angry", "scared", "upset"]}),
  dict(tipo="fill", titulo="How do they feel?", instr="Completa con un adjetivo del recuadro.", banco=["nervous", "tired", "scared", "proud", "bored", "angry", "excited", "worried"], items=[
   "I have an exam tomorrow. I'm [nervous].", "I worked for ten hours. I'm [tired].", "There's a big spider! I'm [scared].", "My son won a prize. I'm very [proud].",
   "There's nothing to do. I'm [bored].", "Somebody broke my phone! I'm [angry].", "We're going to Rapa Nui tomorrow! I'm [excited].", "My dog is sick. I'm [worried]."]),
  dict(tipo="choice", titulo="-ED or -ING?", instr="Encierra la opción correcta.", items=[
   "The film was very {bored|boring*}.", "I'm {interested*|interesting} in music.", "The news was {surprised|surprising*}.", "She was {tired*|tiring} after the trip.",
   "This book is {excited|exciting*}.", "I'm {confused*|confusing}. Can you repeat?", "The storm was {frightened|frightening*}.", "We were {amazed*|amazing} by the view."]),
  dict(tipo="rewrite", titulo="Why do they feel like that?", instr="Une las ideas con because.", cols=1, items=[
   "I'm happy. / It's my birthday. => I'm happy because it's my birthday.", "She's sad. / Her friend moved away. => She's sad because her friend moved away.",
   "They're nervous. / They have a presentation. => They're nervous because they have a presentation.", "He's angry. / He lost his wallet. => He's angry because he lost his wallet.",
   "We're excited. / We are going on a trip. => We're excited because we are going on a trip."]),
  dict(tipo="text", titulo="Complete the text", instr="Completa con adjetivos de sentimientos.", banco=["nervous", "proud", "happy", "scared", "relieved", "excited"], texto=
   "Last week was my first day on a training ship. In the morning I was very [excited] because I love the sea. But when the ship left the port, I was a bit [nervous]. "
   "In the afternoon, there were big waves and I was [scared]. Then the sea was calm again and I was [relieved]. "
   "At the end of the day, the captain said I did a good job. I felt [proud] and very [happy]."),
  dict(tipo="match", titulo="Give advice", instr="Une el sentimiento con un buen consejo.", pares=[
   ("I'm bored.", "Read a book or go for a walk."), ("I'm tired.", "Go to bed early."), ("I'm nervous about the test.", "Study and breathe slowly."),
   ("I'm lonely.", "Call a friend."), ("I'm angry.", "Count to ten and relax."), ("I'm stressed.", "Do some exercise.")]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "I feel nervous before exams.", "Why are you so angry?", "My parents are proud of me.", "She was surprised by the news."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Talking about emotions", texto=
   "Many teenagers feel stressed or worried sometimes. It's normal! Psychologists say that it's important to talk about our feelings. "
   "When you feel sad or lonely, you can talk to a friend, a teacher or your family. Doing sport, listening to music or spending time in nature can help you feel calm. "
   "Sleeping well is very important too: when we are tired, we get angry more easily.",
   vf=[("It's normal to feel worried sometimes.", True), ("Psychologists say we shouldn't talk about feelings.", False), ("Music can help you feel calm.", True), ("When we are tired, we get angry more easily.", True)],
   preguntas=["Who can you talk to when you feel sad? => A friend, a teacher or your family.", "Name two things that help you feel calm. => Doing sport, listening to music or spending time in nature."]),
  dict(tipo="write", titulo="How do you feel when…?", instr="Completa con tus sentimientos.", items=[
   "I feel happy when", "I get nervous when", "I feel bored when", "I'm proud of"]),
 ]),

# ------------------------------------------------------------------ SPORTS
dict(slug="sports", titulo="Sports & Free Time", nivel="2°", cefr="A2",
 objetivo="hablar de deportes y actividades de tiempo libre con play / go / do.",
 goal="talk about sports and hobbies using play, go and do.",
 recordar=[
  "<b>play</b> + deportes con pelota / en equipo: <i>play football, basketball, tennis, volleyball, chess</i>",
  "<b>go</b> + actividades en -ing: <i>go swimming, surfing, running, cycling, fishing, sailing, hiking</i>",
  "<b>do</b> + actividades individuales / artes marciales: <i>do karate, yoga, gymnastics, athletics, exercise</i>",
  "Lugares: court (cancha de tenis/básquet), pitch / field (cancha de fútbol), pool, gym, track · Personas: player, coach, referee, team",
 ],
 ejercicios=[
  dict(tipo="classify", titulo="PLAY, GO or DO?", instr="Clasifica los deportes.", categorias={
   "PLAY": ["football", "tennis", "volleyball", "rugby"], "GO": ["swimming", "surfing", "sailing", "hiking"], "DO": ["karate", "yoga", "gymnastics", "judo"]}),
  dict(tipo="fill", titulo="Complete with play, go or do", instr="Usa la forma correcta.", items=[
   "I [play] basketball on Fridays.", "My dad [goes] fishing every Sunday.", "She [does] yoga in the morning.", "We [play] chess at lunchtime.",
   "They [go] surfing in Reñaca.", "He [does] karate.", "Do you [go] running?", "My sister [plays] volleyball for the school team."]),
  dict(tipo="match", titulo="Match the sport and the equipment", instr="Une el deporte con su implemento.", pares=[
   ("tennis", "racket"), ("surfing", "board"), ("swimming", "goggles"), ("football", "boots"), ("sailing", "boat / sail"), ("cycling", "helmet"), ("fishing", "rod")]),
  dict(tipo="match", titulo="Match the sport and the place", instr="Une el deporte con el lugar.", pares=[
   ("football", "pitch / field"), ("tennis", "court"), ("swimming", "pool"), ("athletics", "track"), ("surfing", "beach"), ("weightlifting", "gym")]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "I {go*|play} swimming twice a week.", "The {referee*|coach} showed a red card.", "She {does*|plays} gymnastics.", "Our team {won*|winned} the match.",
   "He {plays*|goes} rugby.", "I'm good {at*|in} sport.", "We go {to sail|sailing*} in summer.", "The {player|coach*} trains the team."]),
  dict(tipo="text", titulo="Complete the text", instr="Completa con palabras del recuadro.", banco=["team", "plays", "goes", "coach", "match", "won", "does", "pitch"], texto=
   "My cousin Ignacio loves sport. He [plays] football for the school [team]. They train on the [pitch] behind the school every Tuesday. "
   "Their [coach] is very strict. Last Saturday they had an important [match] and they [won] 3-1! Ignacio also [goes] surfing in summer, "
   "and his sister [does] karate."),
  dict(tipo="rewrite", titulo="Write about free time", instr="Escribe oraciones con la información.", cols=2, items=[
   "Tomás / swimming / Mondays => Tomás goes swimming on Mondays.", "Ana and Lucía / tennis / weekends => Ana and Lucía play tennis at the weekend.",
   "my mum / yoga / every day => My mum does yoga every day.", "we / chess / Fridays => We play chess on Fridays."]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "How often do you go cycling?", "My brother plays basketball very well.", "We went sailing last summer.", "Do you do any sport?"]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Water sports in Valparaíso region", texto=
   "The Valparaíso region is great for water sports. In Concón and Reñaca, many young people go surfing and bodyboarding. "
   "In Quintero, you can go sailing and kayaking because the bay is calm. Some people go diving to see fish and old shipwrecks. "
   "The water is cold, so you need a wetsuit. If you don't like the sea, you can play beach volleyball on the sand!",
   vf=[("People go surfing in Reñaca.", True), ("The bay in Quintero is very dangerous.", False), ("You can see shipwrecks when you go diving.", True), ("The water is warm.", False)],
   preguntas=["Why do you need a wetsuit? => Because the water is cold.", "What can you play on the sand? => Beach volleyball."]),
  dict(tipo="write", titulo="Your free time", instr="Escribe sobre tus deportes y pasatiempos.", items=[
   "I play", "I go", "My favourite sportsperson is … because", "I'd like to try"]),
 ]),

# ------------------------------------------------------------------ MUSIC
dict(slug="music", titulo="Music & Instruments", nivel="2°", cefr="A2",
 objetivo="nombrar instrumentos y géneros musicales y expresar preferencias musicales.",
 goal="talk about instruments, music genres and your musical taste.",
 recordar=[
  "Instruments: guitar, bass, drums, piano, keyboard, violin, flute, trumpet, saxophone, harmonica, accordion, charango",
  "Genres: pop, rock, reggaeton, hip-hop, jazz, classical, folk, cumbia, electronic, metal, K-pop",
  "<b>play the</b> + instrumento: <i>I play <b>the</b> guitar.</i> · People: singer, guitarist, drummer, pianist, violinist, band, fan",
  "Opiniones: <i>I'm into rock. · I can't stand… · My favourite band is… · It's catchy / relaxing / noisy.</i>",
 ],
 ejercicios=[
  dict(tipo="fill", titulo="Who plays what?", instr="Escribe la persona que toca el instrumento.", items=[
   "guitar → [guitarist]", "drums → [drummer]", "piano → [pianist]", "violin → [violinist]", "bass → [bassist / bass player]", "trumpet → [trumpeter / trumpet player]",
   "flute → [flautist / flute player]", "voice → [singer]"]),
  dict(tipo="classify", titulo="Classify the instruments", instr="Clasifica según el tipo.", categorias={
   "STRINGS": ["guitar", "violin", "charango", "cello"], "WIND": ["flute", "trumpet", "saxophone", "harmonica"], "PERCUSSION": ["drums", "bombo", "tambourine", "maracas"]}),
  dict(tipo="match", titulo="Match the genre and the description", instr="Une el género con la descripción.", pares=[
   ("classical", "Beethoven and Mozart"), ("cueca", "Chile's national dance"), ("reggaeton", "Latin urban music with a strong beat"), ("jazz", "music born in New Orleans"),
   ("rock", "electric guitars and drums"), ("K-pop", "pop music from South Korea")]),
  dict(tipo="choice", titulo="Choose the correct option", instr="Encierra la opción correcta.", items=[
   "She plays {the*|–} piano.", "I {listen*|hear} to music every day.", "I'm {into*|in} rock music.", "He is a great {drum|drummer*}.",
   "This song is very {catchy*|catching}.", "{Who's*|Whose} your favourite singer?", "They went to a {concert*|concerto} last night.", "I listen {to*|–} reggaeton."]),
  dict(tipo="text", titulo="Complete the text", instr="Completa con palabras del recuadro.", banco=["band", "singer", "drums", "concert", "fans", "songs", "guitar", "album"], texto=
   "My brother has a rock [band] with three friends. He plays the electric [guitar] and his friend Joaquín plays the [drums]. "
   "Their [singer], Catalina, has an amazing voice. They write their own [songs] in Spanish and English. Next month they are going to record their first [album]. "
   "Last Saturday they gave a [concert] at a café in Cerro Alegre. There were a lot of [fans]!"),
  dict(tipo="rewrite", titulo="Write questions", instr="Escribe la pregunta para cada respuesta.", cols=2, items=[
   "I like pop and rock. => What kind of music do you like?", "Yes, I play the guitar. => Do you play an instrument?",
   "My favourite singer is Mon Laferte. => Who is your favourite singer?", "I listen to music on my phone. => How do you listen to music?"]),
  dict(tipo="order", titulo="Put the words in order", instr="Ordena las palabras.", items=[
   "My grandfather plays the accordion.", "What kind of music are you into?", "I can't stand very loud music.", "Violeta Parra was a famous Chilean singer."]),
  dict(tipo="reading", titulo="Read and answer", instr="Lee y responde.", titulo_texto="Music from Valparaíso", texto=
   "Valparaíso is a city full of music. In the bars of the port, people play cumbia, bolero and 'cueca chora', a fast and happy version of the cueca. "
   "Many street musicians play the guitar, the accordion or the trumpet in the squares. The city also has an important music school and a festival every summer. "
   "Some famous Chilean bands, like Los Jaivas, started in the Valparaíso region.",
   vf=[("Valparaíso has a lot of music.", True), ("'Cueca chora' is slow and sad.", False), ("Street musicians play in the squares.", True), ("Los Jaivas started in Santiago.", False)],
   preguntas=["What instruments do street musicians play? => The guitar, the accordion or the trumpet.", "What music do people play in the bars? => Cumbia, bolero and cueca chora."]),
  dict(tipo="write", titulo="Your musical taste", instr="Escribe sobre tus gustos musicales.", items=[
   "I'm into", "My favourite singer / band is … because", "I play / I'd like to play", "I can't stand"]),
 ]),
]
