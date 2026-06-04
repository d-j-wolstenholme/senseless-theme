#!/usr/bin/env python3
"""Senseless — port the 5 Guides articles verbatim from the Master Page DB into the `guides` blog.
REST article create (content = allowed via API). FAQ -> custom.faq json metafield (accordion +
FAQPage schema). meta via global.title_tag/description_tag. template_suffix=guides. Published.
Stale /pages/choosing-your-strength -> /pages/the-senseless-system. botox-bruising link dropped
(article not in scope). Sibling cross-links does-botox-hurt <-> do-lip-fillers-hurt added.
"""
import os, sys, json, urllib.request, urllib.error
TOKEN=os.environ["SHOPIFY_ACCESS_TOKEN"]
BLOG=127881740636
BASE="https://senseless-numbing.myshopify.com/admin/api/2024-10"

def rest(path, payload):
    req=urllib.request.Request(BASE+path, data=json.dumps(payload).encode(),
        headers={"X-Shopify-Access-Token":TOKEN,"Content-Type":"application/json"}, method="POST")
    try:
        return json.load(urllib.request.urlopen(req,timeout=40)), None
    except urllib.error.HTTPError as e:
        return None, e.read().decode()[:300]

SYS="/pages/the-senseless-system"

A1_BODY="""<p>You have had your Botox, the mirror looks exactly the same, and the natural question follows: how long until it actually works? The reassuring answer is that Botox is not meant to do anything straight away. Here is the realistic timeline, what is happening while you wait, and why patience is part of the process.</p>
<blockquote><p><strong>The short answer:</strong> Botox usually starts to work within 3 to 4 days, with the full effect visible around 10 to 14 days after treatment. It then typically lasts about 3 to 4 months before gradually wearing off.</p></blockquote>
<h2>The Botox timeline</h2>
<p>Botox works gradually as it takes effect on the treated muscles. For most people the first subtle changes appear within a few days, building steadily until the full result is in place at around two weeks. Nothing is wrong if you see no change on day one — that is exactly what is expected.</p>
<h2>What's happening day by day</h2>
<ul><li><strong>Days 1 to 2</strong> — usually no visible change. This is normal.</li><li><strong>Days 3 to 5</strong> — many people notice the first signs as movement in the treated area begins to soften.</li><li><strong>Days 7 to 10</strong> — the effect becomes clearer and more settled.</li><li><strong>Days 10 to 14</strong> — the full result is typically in place. This is the point at which practitioners assess and, if needed, top up.</li></ul>
<h2>What affects how quickly Botox works</h2>
<ul><li>The area treated and the dose used</li><li>Your individual response — everyone metabolises a little differently</li><li>Whether it is your first treatment or a repeat</li><li>The strength of the muscles being treated</li></ul>
<p>None of these are things to worry about; they simply mean timelines vary slightly from person to person.</p>
<h2>How long does Botox last?</h2>
<p>Once it has fully taken effect, Botox generally lasts around 3 to 4 months before movement gradually returns and the look softens. With regular treatment, some people find results last a little longer over time. Your practitioner will recommend a maintenance schedule that suits you.</p>
<h2>While you wait</h2>
<ul><li>Don't judge the result before two weeks — it isn't finished yet</li><li>Follow your practitioner's aftercare guidance in the first 24 hours</li><li>If a review is planned, it is usually at the two-week mark</li><li>Resist comparing day-three to someone else's day-fourteen photo</li></ul>
<h2>Preparing for your next appointment</h2>
<p>Comfort is the part of the appointment you can plan for. If you would like to feel less of the process, a topical preparation used in line with your practitioner's guidance is a simple step. Senseless is made for aesthetic appointments — matched to the treatment and applied as your practitioner advises.</p>
<p><a href="/collections/numbing-cream-for-botox">See numbing cream for Botox &rarr;</a></p>
<p><a href="/blogs/guides/does-botox-hurt">Does Botox hurt? &rarr;</a></p>"""
A1_FAQ=[
 {"question":"When does Botox start working?","answer":"<p>Usually within 3 to 4 days, when the first subtle softening appears in the treated area.</p>"},
 {"question":"How long until Botox is fully working?","answer":"<p>Around 10 to 14 days for most people. This is when the full effect is in place and practitioners review.</p>"},
 {"question":"How long does Botox last?","answer":"<p>Typically about 3 to 4 months before it gradually wears off, varying with the person and the area.</p>"},
 {"question":"Why hasn't my Botox worked yet?","answer":"<p>If it has been only a few days, that is completely normal — give it the full two weeks. If there is still no change after that, speak to your practitioner.</p>"},
 {"question":"Does Botox work faster the more you have it?","answer":"<p>The onset is broadly similar, but some people find results last longer with regular treatment. Your practitioner can advise on your pattern.</p>"},
]

A2_BODY="""<p>Good aftercare is the quiet half of a good result. The appointment shapes your lips; the days that follow decide how comfortably they settle. This is a complete, honest guide to lip filler aftercare — what is normal, what helps, what to avoid, and when to call your practitioner — written to sit alongside their advice, never to replace it.</p>
<blockquote><p><strong>The short answer:</strong> mild swelling, tenderness, and the odd small bruise are normal for the first day or two and usually settle within about two weeks. Treat the area gently, keep it clean, avoid heat and strenuous exercise for the first 24 to 48 hours, and follow your practitioner's specific instructions.</p></blockquote>
<h2>What's normal after lip filler</h2>
<p>In the hours after your appointment, it is normal for the lips to feel tender, look fuller than the final result, and show some swelling. Small bruises, a little asymmetry while swelling is uneven, and slight tightness are all common and usually temporary. This is recovery, not a problem. It tends to ease quickly, and the final shape becomes clear once the swelling fully settles.</p>
<p>Everyone heals at their own pace. If anything worries you, your practitioner is the right person to ask.</p>
<h2>Lip filler healing stages, day by day</h2>
<p>A typical timeline looks something like this. Yours may differ:</p>
<ul><li><strong>Day of treatment</strong> — tenderness, swelling, and possible small bruises. The lips look bigger than the end result.</li><li><strong>Days 1 to 2</strong> — swelling often peaks. This is usually the most noticeable stage, and it settles from here.</li><li><strong>Days 3 to 5</strong> — swelling and bruising begin to fade. The lips start to look more like themselves.</li><li><strong>Week 1</strong> — most of the visible swelling has gone for many people. Minor lumps or unevenness can still be felt as things settle.</li><li><strong>Week 2 and beyond</strong> — the filler settles into its final position and the result becomes clear. This is usually when practitioners review, if a review is planned.</li></ul>
<h2>The do's</h2>
<ul><li>Stay hydrated and rest in the first 24 hours</li><li>Use a cool compress gently if your practitioner advises it, to ease swelling</li><li>Sleep with your head slightly elevated for the first night or two</li><li>Keep the area clean and handle it gently</li><li>Eat and drink carefully while the area is numb or tender</li><li>Follow every instruction your practitioner gives you — theirs is the advice that counts</li></ul>
<h2>The don'ts (first 24 to 48 hours)</h2>
<ul><li>Avoid touching, pressing, or massaging the lips unless your practitioner tells you to</li><li>Avoid heat — saunas, steam rooms, hot yoga, sunbeds, and very hot drinks</li><li>Avoid strenuous exercise for the first day or two</li><li>Avoid alcohol, which can worsen swelling and bruising</li><li>Avoid makeup on the lips until your practitioner says it is fine</li><li>Avoid flying immediately afterwards if your practitioner has advised against it</li></ul>
<h2>Keeping the area clean</h2>
<p>In the days after an appointment, the treated area benefits from gentle, clean handling. The Senseless Foaming Cleanser is built for exactly that window — an antibacterial cleansing foam that respects skin that has just had something done. Gentle on the area, simple to use, and made for aftercare rather than borrowed from your usual routine.</p>
<p><a href="/products/foaming-cleanser">View the Foaming Cleanser &rarr;</a></p>
<h2>When to contact your practitioner</h2>
<p>Most recovery is uneventful. Contact your practitioner promptly, though, if you notice anything that does not feel right — for example, pain that is severe or increasing rather than easing, swelling that worsens after the first couple of days, signs of infection, or any blanching or unusual colour change in the lips or surrounding skin. When in doubt, get in touch with them. That is what they are there for, and acting early is always sensible.</p>
<h2>Preparing for next time</h2>
<p>Comfort starts before the appointment, not after it. If your last booking felt like more than you would like, preparation is the part you can change. For lip fillers, Clinical Strength suits most appointments, with Advanced there for longer or more sensitive sessions — applied in line with your practitioner's guidance.</p>
<p><a href="/collections/numbing-cream-for-lip-fillers">See numbing cream for lip fillers &rarr;</a></p>
<p><a href="%SYS%">Find your strength &rarr;</a></p>""".replace("%SYS%",SYS)
A2_FAQ=[
 {"question":"How long does lip filler swelling last?","answer":"<p>Swelling often peaks in the first day or two and settles for most people within about two weeks. Yours may differ — your practitioner can tell you what to expect for your treatment.</p>"},
 {"question":"Can I kiss after lip fillers?","answer":"<p>It is generally advised to avoid pressure on the lips for the first day or so. Follow your practitioner's specific guidance.</p>"},
 {"question":"When can I exercise after lip fillers?","answer":"<p>Many practitioners suggest avoiding strenuous exercise for the first 24 to 48 hours. Check what your practitioner recommends.</p>"},
 {"question":"When can I wear lipstick or makeup again?","answer":"<p>Usually once the area has settled and your practitioner is happy — often after the first day or two. Confirm with them.</p>"},
 {"question":"Is it normal to have lumps after lip filler?","answer":"<p>Feeling small, even lumps as filler settles can be normal in the early days. If lumps persist, grow, or concern you, contact your practitioner.</p>"},
]

A3_BODY="""<p>Botox for jowls is one of the more misunderstood treatments, mostly because expectations and reality don't always line up. It can soften the lower face for the right person, but it works in a specific way and isn't a substitute for everything. Here is an honest explanation of what Botox for jowls actually does, who it suits, and what to expect.</p>
<blockquote><p><strong>The short answer:</strong> Botox for jowls works by relaxing the muscles that pull the lower face downward — often through a &ldquo;Nefertiti lift&rdquo; along the jaw and neck, or masseter Botox — which can soften the jawline. It suits some causes of jowls better than others, and the result is subtle rather than a facelift.</p></blockquote>
<h2>What "Botox for jowls" actually means</h2>
<p>Jowls form for several reasons, including the downward pull of certain muscles, changes in volume, and skin laxity. Botox addresses one part of that picture: muscle activity. By relaxing specific muscles that tug the lower face down, a practitioner can allow the jawline to sit a little smoother. It is a refinement, not a reconstruction.</p>
<h2>How it works</h2>
<p>Two approaches come up most often:</p>
<ul><li><strong>The Nefertiti lift</strong> — small amounts of Botox placed along the jawline and upper neck (the platysma muscle), easing the downward pull and softening the jaw's edge</li><li><strong>Masseter Botox</strong> — relaxing the chewing muscle at the angle of the jaw, which slims a strong or square jaw and can affect how the lower face reads</li></ul>
<p>Which, if either, suits you depends entirely on what is creating your jowls — something only a practitioner can assess in person.</p>
<h2>What results to expect</h2>
<p>Botox for jowls is best understood as subtle softening rather than lifting heavy, sagging skin. It tends to help most where muscle pull is part of the cause, and less where the main factor is significant skin laxity. If your expectations are realistic — a smoother, slightly more defined lower face rather than a dramatic lift — many people are pleased with it.</p>
<h2>Is it right for you?</h2>
<p>This is genuinely a consultation question. A good practitioner will look at the cause of your jowls and tell you honestly whether Botox is the right tool, whether something else (such as filler or other treatments) would suit better, or whether a combination makes sense. Beware anyone promising a facelift from an injectable.</p>
<h2>What to expect at the appointment</h2>
<p>The appointment itself is quick, with a few precise injections. As with any Botox, you may notice small bumps or pinpoint marks that settle shortly after, and results develop over the following days to a couple of weeks. Your practitioner will give you aftercare guidance. For comfort specifics, see our guide on <a href="/blogs/guides/does-botox-hurt">whether Botox hurts</a>.</p>
<h2>Preparing for your appointment</h2>
<p>If you would like to feel less of the process, a topical preparation used in line with your practitioner's guidance is a simple step. Senseless is made for aesthetic appointments — matched to the treatment and applied as your practitioner advises.</p>
<p><a href="/collections/numbing-cream-for-botox">See numbing cream for Botox &rarr;</a></p>
<p><a href="%SYS%">Find your strength &rarr;</a></p>""".replace("%SYS%",SYS)
A3_FAQ=[
 {"question":"Does Botox lift jowls?","answer":"<p>It can soften the appearance of jowls where muscle pull is part of the cause, by relaxing the muscles that draw the lower face down. It is subtle, and it works better for some causes than others.</p>"},
 {"question":"What is masseter Botox for jowls?","answer":"<p>Relaxing the masseter (the chewing muscle at the jaw angle) can slim a strong jaw and influence how the lower face looks. Whether it helps your jowls specifically is a consultation question.</p>"},
 {"question":"How long does Botox for jowls last?","answer":"<p>Botox results generally last a few months before gradually wearing off. Your practitioner can give you a realistic timeframe for the area treated.</p>"},
 {"question":"Does Botox for jowls hurt?","answer":"<p>The injections are quick and most people find them mild. Numbing and an experienced injector keep it comfortable for most.</p>"},
 {"question":"Is Botox or filler better for jowls?","answer":"<p>It depends on the cause. Botox addresses muscle pull; filler addresses volume; sometimes a combination suits best. A practitioner will advise based on your face.</p>"},
]

A4_BODY="""<p>Botox is one of the quickest aesthetic appointments there is, and one of the most asked-about when it comes to discomfort. The honest answer is that you will feel something — these are injections — but most people are surprised by how little, and how fast it is over. Here is what Botox actually feels like, what shapes the experience, and how clients keep it comfortable.</p>
<blockquote><p><strong>The short answer:</strong> Botox involves a few quick injections with a very fine needle. Most people describe a brief pinch or sting rather than real pain, and the appointment is usually over in minutes. Comfort varies from person to person, and numbing can help.</p></blockquote>
<h2>What Botox actually feels like</h2>
<p>Botox is delivered through very fine needles, in small amounts, across a handful of points. Most clients describe each injection as a quick sting or a tiny pinch, sometimes with a brief pressure, and then it is done. Because the needles are fine and the amounts small, many people find it more manageable than they expected. The whole thing is usually finished in a few minutes.</p>
<h2>Does Botox hurt more than fillers?</h2>
<p>Most people find Botox less intense than lip fillers. The lips are densely packed with nerve endings, whereas the forehead and the areas around the eyes tend to register less. It is not a rule — sensitivity is individual, and the area being treated matters — but if you have had lip fillers and found them manageable, Botox usually feels lighter. If you are weighing both up, our guide to <a href="/blogs/guides/do-lip-fillers-hurt">whether lip fillers hurt</a> sits alongside this one.</p>
<h2>What affects how much it hurts</h2>
<ul><li>The area being treated — frown lines, forehead, and crow's feet can each feel slightly different</li><li>The fineness of the needle and your practitioner's technique</li><li>Your own sensitivity and how you feel about needles on the day</li><li>Whether numbing is used</li><li>How relaxed you are walking in</li></ul>
<p>As with any injectable, an experienced, unhurried practitioner makes the biggest difference.</p>
<h2>The role of numbing</h2>
<p>Many Botox appointments are quick enough that numbing is not always used, but plenty of practitioners offer it, and plenty of clients prefer to prepare. A topical numbing preparation applied beforehand, in line with your practitioner's guidance, is a common way to take the edge off the anticipation as much as the sensation.</p>
<p>This is where Senseless fits — a topical preparation made for aesthetic appointments, used ahead of the chair to support a more comfortable experience. Always tell your practitioner what you have applied and when, and follow their protocol.</p>
<p><a href="/collections/numbing-cream-for-botox">See numbing cream for Botox &rarr;</a></p>
<p><a href="%SYS%">Find your strength &rarr;</a></p>
<h2>After your appointment</h2>
<p>Small raised bumps at the injection points, a little redness, and occasionally a pinpoint bruise are normal in the first short while and tend to settle quickly. Your practitioner will give you aftercare guidance — commonly, staying upright for a few hours and avoiding rubbing the area. Follow what they tell you.</p>
<h2>How to prepare for a calmer appointment</h2>
<ul><li>Choose an experienced, qualified practitioner</li><li>Say if you are nervous — it changes how the appointment is paced</li><li>Ask about numbing in advance, and prepare with a topical preparation if your practitioner is happy for you to</li><li>Be rested, and follow any pre-appointment guidance you are given</li><li>Breathe steadily through each injection</li></ul>""".replace("%SYS%",SYS)
A4_FAQ=[
 {"question":"Is Botox painful?","answer":"<p>Most people find it mild — a quick pinch or sting at each point rather than real pain, over in minutes. It varies between individuals.</p>"},
 {"question":"How painful is Botox?","answer":"<p>For most, it sits at the low end of the scale, especially with a fine needle and an experienced injector. Sensitivity and the treated area both play a part.</p>"},
 {"question":"Does Botox hurt more than fillers?","answer":"<p>Usually less. The lips carry more nerve endings than the forehead or around the eyes, so lip fillers tend to feel more intense than Botox for most people.</p>"},
 {"question":"Can you numb before Botox?","answer":"<p>Some practitioners offer numbing, and some clients prepare with a topical preparation beforehand, used per their practitioner's guidance. Confirm your plan with your practitioner.</p>"},
 {"question":"Does Botox in the forehead hurt more than crow's feet?","answer":"<p>It varies. Different areas can feel slightly different, but all are typically quick and manageable.</p>"},
]

A5_BODY="""<p>Lip fillers involve injections into one of the more sensitive areas of the face, so there is some sensation. Most people feel it. Most describe it as mild to moderate rather than severe, and most are surprised by how quickly it passes. The honest answer to whether lip fillers hurt is that it depends — on you, on your practitioner, and on how the appointment is run. The more useful answer is that a modern lip filler appointment is built around keeping you comfortable, and a good deal of the experience is set before the needle ever appears.</p>
<blockquote><p><strong>The short answer:</strong> lip fillers usually feel like a quick sting as the needle goes in, followed by a sense of pressure as the filler is placed. With numbing and an experienced injector, most clients find it very manageable, and it is over quickly.</p></blockquote>
<p>This is a guide to what lip filler injections actually feel like, what makes the difference between a sharp, calm appointment and an uncomfortable one, and how clients prepare.</p>
<h2>What lip fillers actually feel like</h2>
<p>Most clients describe a quick sting or pinch as the needle enters, then a feeling of pressure as the filler is placed and shaped. The lips are rich in nerve endings, which is why the area registers more than a cheek or a jawline would. Appointments are usually short, and the sensation arrives in brief moments rather than as one continuous thing. It tends to settle the instant each injection is done.</p>
<p>It is common to feel more on the first pass and less as the appointment goes on, as the area adjusts and any numbing takes hold.</p>
<h2>What affects how much it hurts</h2>
<p>No two appointments feel the same. Several things shape where yours lands on the pain scale:</p>
<ul><li>Your own pain threshold, and how you feel about needles on the day</li><li>The technique your practitioner uses — a fine needle and a cannula feel different, and unhurried, precise placement matters</li><li>Whether numbing is used, and in what form</li><li>Where you are in your cycle, and how rested and hydrated you are</li><li>How anxious or relaxed you are walking in</li></ul>
<p>The single biggest factor is usually the practitioner. An experienced injector who works calmly, communicates as they go, and does not rush changes the entire character of the appointment.</p>
<h2>The role of numbing</h2>
<p>Most practitioners take comfort seriously. Many apply a topical numbing cream before they begin, and some dermal fillers include an ingredient that aids comfort as the treatment progresses. For clients who want more, a number of practitioners offer a dental-style block.</p>
<p>Plenty of clients also prepare beforehand with their own topical preparation, applied in line with their practitioner's guidance. This is where Senseless fits. Senseless is a topical preparation made for aesthetic appointments, used ahead of the chair to support a more comfortable experience. It does not replace your practitioner's protocol — it sits alongside it. Always tell your practitioner what you have applied, and when.</p>
<p><a href="/collections/numbing-cream-for-lip-fillers">See the range built for this appointment &rarr;</a></p>
<h2>"Painless lip fillers" — is that a fair promise?</h2>
<p>You will see the phrase. We would gently steer you away from it. Injections create sensation, and anyone promising a completely painless appointment is overselling something they cannot guarantee. The honest goal was never &ldquo;painless.&rdquo; It is comfortable, calm, and well-managed — an experienced practitioner you trust, and preparation that suits you. Aim for that, and the question of whether it hurts tends to answer itself.</p>
<h2>After your appointment</h2>
<p>Most of what you feel afterwards is recovery, not the injection. Tenderness, mild swelling, and the occasional small bruise are common for a day or two, and the lips can feel tight or sensitive as everything settles. This is normal, and it usually eases quickly. Treat the area gently, keep it clean while it recovers, and follow whatever aftercare advice your practitioner gives you. Our <a href="/blogs/guides/lip-filler-aftercare">lip filler aftercare guide</a> walks through the days that follow.</p>
<h2>How to prepare for a calmer appointment</h2>
<p>Preparation is the part you control, and it does more than most people expect:</p>
<ul><li>Choose an experienced, qualified practitioner, and look at their actual work</li><li>Say if you are nervous — good injectors adjust their pace and talk you through it</li><li>Ask about numbing in advance, and prepare with a topical preparation if your practitioner is happy for you to</li><li>Be rested and well hydrated, and follow any guidance on avoiding things that thin the blood</li><li>Breathe slowly and steadily through each injection</li></ul>
<p>Get the preparation right and the rest is simply the appointment doing what it is designed to do.</p>
<h2>The Senseless approach</h2>
<p>Senseless is built for the appointment, not around the fear of it. For lip fillers, Clinical Strength suits most bookings, and Advanced is there for longer sessions, larger volumes, or lips that run sensitive. Match the preparation to the appointment, apply it the way your practitioner advises, and walk in ready. If you are weighing it against another treatment, our guide to <a href="/blogs/guides/does-botox-hurt">whether Botox hurts</a> sits alongside this one.</p>
<p><a href="/collections/numbing-cream-for-lip-fillers">Shop for lip fillers &rarr;</a></p>
<p><a href="%SYS%">Not sure which to choose? Find your strength &rarr;</a></p>""".replace("%SYS%",SYS)
A5_FAQ=[
 {"question":"Are lip fillers painful?","answer":"<p>Most clients find them mild to moderate rather than painful, particularly with numbing and an experienced injector. The lips are sensitive, so you will feel something, but it is usually brief and very manageable.</p>"},
 {"question":"How painful are lip fillers compared to other treatments?","answer":"<p>Many people find lip injections more noticeable than something like Botox, simply because the lips carry more nerve endings. It varies considerably from person to person, and from one appointment to the next.</p>"},
 {"question":"Do lip injections hurt the first time?","answer":"<p>The first appointment often feels more daunting, because you do not yet know what to expect. Most clients find it more manageable than they feared, and easier still at follow-up appointments.</p>"},
 {"question":"Can you numb before lip fillers?","answer":"<p>Many practitioners apply a topical numbing cream before treatment, and some clients prepare with their own beforehand, used in line with their practitioner's guidance. Always confirm your plan with your practitioner first.</p>"},
 {"question":"How can I make lip fillers hurt less?","answer":"<p>Choose a skilled practitioner, prepare well, ask about numbing, stay as relaxed as you can, and follow any pre-appointment advice. Most of your comfort is decided before the needle.</p>"},
 {"question":"Is the soreness afterwards normal?","answer":"<p>Yes. Tenderness, mild swelling, and small bruises for a day or two are common and usually settle quickly. If anything concerns you or does not improve, contact your practitioner.</p>"},
]

ARTICLES=[
 dict(handle="how-long-does-botox-take-to-work", title="How Long Does Botox Take to Work",
      mt="How Long Does Botox Take to Work? The Full Timeline",
      md="How long does Botox take to work? It usually starts in 3 to 4 days and reaches full effect around 10 to 14 days. The day-by-day timeline and what affects it.",
      summary="Botox usually starts in 3 to 4 days and reaches full effect around 10 to 14 days — the day-by-day timeline and what affects it.",
      body=A1_BODY, faq=A1_FAQ),
 dict(handle="lip-filler-aftercare", title="Lip Filler Aftercare — Complete Guide",
      mt="Lip Filler Aftercare: The Complete Day-by-Day Guide",
      md="A complete lip filler aftercare guide — what's normal, healing stages day by day, the dos and don'ts, and when to call your practitioner. Plus how to keep the area clean.",
      summary="What's normal, healing stages day by day, the dos and don'ts, and when to call your practitioner.",
      body=A2_BODY, faq=A2_FAQ),
 dict(handle="botox-for-jowls", title="Botox for Jowls — What to Expect",
      mt="Botox for Jowls: What It Can (and Can't) Do",
      md="Botox for jowls explained — how it softens the lower face, the Nefertiti lift and masseter approaches, who it suits, and what results to realistically expect.",
      summary="How Botox softens the lower face — the Nefertiti lift and masseter approaches, who it suits, and what to realistically expect.",
      body=A3_BODY, faq=A3_FAQ),
 dict(handle="does-botox-hurt", title="Does Botox Hurt?",
      mt="Does Botox Hurt? What to Expect & How to Prepare",
      md="Does Botox hurt? What the injections actually feel like, whether it hurts more than fillers, what affects discomfort, and how to prepare for a calmer appointment.",
      summary="What the injections actually feel like, whether it hurts more than fillers, and how to prepare for a calmer appointment.",
      body=A4_BODY, faq=A4_FAQ),
 dict(handle="do-lip-fillers-hurt", title="Do Lip Fillers Hurt?",
      mt="Do Lip Fillers Hurt? What to Expect & How to Prepare",
      md="Do lip fillers hurt? An honest look at what lip filler injections feel like, what affects discomfort, and how to prepare for a calmer appointment.",
      summary="An honest look at what lip filler injections feel like, what affects discomfort, and how to prepare for a calmer appointment.",
      body=A5_BODY, faq=A5_FAQ),
]

for a in ARTICLES:
    # stale-link guard
    assert "/pages/choosing-your-strength" not in a["body"], a["handle"]+" still has choosing-your-strength"
    assert "/pages/how-it-works" not in a["body"], a["handle"]+" has how-it-works"
    assert "botox-bruising" not in a["body"], a["handle"]+" has botox-bruising"
    payload={"article":{
        "title":a["title"],"handle":a["handle"],"author":"Senseless",
        "body_html":a["body"],"summary_html":"<p>"+a["summary"]+"</p>",
        "published":True,"template_suffix":"guides",
        "metafields":[
            {"namespace":"global","key":"title_tag","type":"single_line_text_field","value":a["mt"]},
            {"namespace":"global","key":"description_tag","type":"single_line_text_field","value":a["md"]},
            {"namespace":"custom","key":"faq","type":"json","value":json.dumps(a["faq"],ensure_ascii=False)},
        ]}}
    res,err=rest(f"/blogs/{BLOG}/articles.json",payload)
    if err: print("ERR",a["handle"],err)
    else: print("OK",a["handle"],"id",res["article"]["id"],"faq",len(a["faq"]),"len",len(a["body"]))
