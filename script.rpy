init python:
    import random
    
    def roll_d6():
        return random.randint(1, 6)

    # list every character base name you use in "show" statements
    _all_characters = ["luna", "kaique", "mila", "theo", "alice", "leonardo", "diretora"]
    def hide_all_characters():
        for c in _all_characters:
            try:
                renpy.hide(c)
            except Exception:
                pass

define l = Character("Luna", color="#6AAFE6")
define k = Character("Kaique", color="#E2956A")
define m = Character("Mila", color="#A36AE6")
define t = Character("Theo", color="#6AE699")
define a = Character("Alice", color="#E66A98")
define leonardo = Character("Leonardo", color="#888888")
define diretora = Character("Diretora", color="#4444AA")

default trust_alice = False
default targeted_by_aggressors = False
default discovered_profiles = False
default leonardo_in_crisis = False

label start:
    scene bg school_hall with fade

    "Ato 1 — O Começo da Semana"
    show luna neutral at left
    l "É meu primeiro dia aqui... tudo parece grande demais."
    $ hide_all_characters()
    show kaique smile at left
    k "Calma, Luna. Eu te apresento pro pessoal depois do recreio."
    $ hide_all_characters()
    show mila excited at left
    m "Tem cartazes do clube de ciências no mural. Depois eu mostro como achar informações sobre projetos."
    $ hide_all_characters()
    show theo grin at left
    t "Bem-vinda à selva escolar. Se alguém te chatear por aqui, eu faço uma piada e a situação some. Pode contar comigo."
    $ hide_all_characters()
    "No corredor, Alice recebe bilhetes e risadinhas de alguns colegas."
    show luna sad at left
    a "Por favor... só parem com isso..."

    # Escolha: Intervir ou Ignorar
    menu:
        "O que vocês fazem?"
        "Intervir — tentar ajudar Alice":
            $ r = roll_d6()
            if r >= 4:
                $ trust_alice = True
                $ hide_all_characters()
                show kaique shouting at left 
                k "Ei, chega! Isso não é brincadeira."
                "Kaique se coloca à frente com voz firme; sua influência acalma os agressores."
                $ hide_all_characters()
                show luna thoughtful at left
                l "Notei que os bilhetes vêm sempre da mesma turma — eles usam o mesmo tipo de caneta."
                "Luna aponta o detalhe; observadora, ela ajuda a explicar a situação."
                $ hide_all_characters()
                show mila determined at left
                m "Vou anotar os nomes e procurar posts antigos nas redes da escola."
                show theo confident at left
                t "Não se preocupa, a gente tá com você — e eu prometo umas piadas ruins pro resto da semana."
                "Alice parece aliviada e confia mais no grupo."
            else:
                $ targeted_by_aggressors = True
                $ hide_all_characters()
                show kaique hesitant at left
                k "E se..."
                "Kaique hesita; tentar intervir falha e os agressores marcam o grupo como alvo."
                show luna sad at left
                l "Estão me olhando estranho... Vou ficar na minha..."
                show theo nervous at left
                t "Ei, rindo para não chorar..."
        "Ignorar — evitar envolvimento":
            $ targeted_by_aggressors = True
            "Vocês recuam. Os agressores continuam; Alice fica mais isolada."
            m "Isso não parece certo... mas se nos metermos podemos virar alvo também."
            t "Pelo menos o lanche está intacto."

    "Ato 2 — O Desaparecimento"
    scene bg classroom_day with dissolve
    "No dia seguinte, Alice não aparece."
    if trust_alice:
        a "Desculpem... eu precisava fugir por um dia, mas queria avisar vocês."
    else:
        "Circulam boatos de que ela 'fugiu' por pressão."

    "À tarde, vocês acham uma mensagem anônima:"
    "\"A escola tem segredos. O verdadeiro monstro está no pátio.\""

    "Mila faz checagens nas redes internas da escola."
    menu:
        "Quem lidera a investigação?"
        "Mila pesquisa (teste de Pesquisa)":
            $ r = roll_d6()
            if r >= 2:
                $ discovered_profiles = True
                m "Encontrei contas falsas criadas nos últimos meses. Elas postam insultos contra Alice e outros alunos."
                "Mila acha rastros digitais rapidamente — sua empolgação vira vantagem prática."
            else:
                m "Há muitos perfis; preciso de mais tempo."
        "Luna observa (teste de Observadora)":
            $ r = roll_d6()
            if r >= 4:
                $ discovered_profiles = True
                l "Reparei num padrão: horários parecidos de postagem. Deve haver uma origem única."
                "Luna liga detalhes que outros não viram."
            else:
                l "Sinto que tem algo, mas não sei onde procurar."
        "Kaique tenta acalmar a turma (teste de Influência)":
            $ r = roll_d6()
            if r >= 4:
                "Kaique consegue evitar brigas enquanto vocês investigam."
                k "Gente, vamos manter a calma e conversar antes de acusar alguém."
            else:
                "Ele falha em acalmar; a tensão cresce."

    if discovered_profiles:
        "As pistas apontam para alguém que conhece bem a escola."
        "Vocês decidem confrontar a área do pátio à noite."

    "Ato 3 — As Sombras no Pátio"
    scene bg school_night with fade
    show leonardo awkward at center
    "No pátio vazio, Leonardo aparece. Ele confessará?"
    leonardo "Eu criei os perfis... queria ensinar uma lição aos valentões."
    "Ele parece extremamente magoado e perdido."

    # Confronto emocional — uso de habilidades para convencer
    "Cada personagem pode tentar uma abordagem. Escolha quem fala com Leonardo."
    menu:
        "Quem tenta convencer Leonardo?"
        "Luna — Observadora (empatia calma)":
            $ r = roll_d6()
            if r >= 3:
                $ leonardo_in_crisis = False
                l "Você não precisa carregar isso sozinho. Vi detalhes que mostram que você sofreu também."
                "Luna se aproxima com cuidado; sua tranquilidade faz Leonardo hesitar e, então, ceder."
                leonardo "Talvez... eu precise de ajuda."
            else:
                l "Não sei o que dizer."
        "Kaique — Influência (autoridade social)":
            $ r = roll_d6()
            if r >= 4:
                $ leonardo_in_crisis = False
                k "Ouça: nós podemos consertar isso juntos. Eu não quero que ninguém sofra."
                "Kaique usa sua posição para oferecer uma rota segura — Leonardo se comove."
                leonardo "Se vocês realmente me ajudarem..."
            else:
                k "Não adianta falar assim agora."
        "Mila — Pesquisa (mostrar evidências)":
            $ r = roll_d6()
            if r >= 4:
                $ leonardo_in_crisis = False
                m "Encontrei suas postagens e o que motivou você. Vocês podem pedir ajuda sem destruir outros."
                leonardo "Você entendeu... eu só queria que parassem."
            else:
                m "Tenho dados, mas não consigo explicar direito."
        "Theo — Improvisar (abordagem leve)":
            $ r = roll_d6()
            if r >= 4:
                $ leonardo_in_crisis = False
                t "Cara, eu já errei também. Posso te mostrar um truque pra aliviar a cabeça agora?"
                "Theo consegue quebrar o gelo com humor na hora certa; Leonardo ri, relaxa e aceita conversar."
                leonardo "Talvez... eu precise de amigos."
            else:
                t "Hmm... talvez meu plano não funcione."

    if leonardo_in_crisis:
        "A tentativa falha: Leonardo foge, assustado. Vocês precisam avisar a direção."
        diretor_call "Vocês fizeram bem em alertar. Vamos cuidar disso."
    else:
        "Leonardo se arrepende e pede ajuda. O grupo convence-no a procurar apoio."
        "Vocês voltam para casa com a sensação de que fizeram a coisa certa."

    "Epílogo"
    scene bg school_day with dissolve
    "A direção lança um projeto anti-bullying liderado pelos alunos. Alice volta mais confiante."
    "Última cena: um novo estudante entra pela porta... vocês sorriem, prontos pra agir."

    return
