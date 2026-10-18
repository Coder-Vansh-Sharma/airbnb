#!/usr/bin/env python3
"""
Expands prompt catalog into hundreds of high-detail prompts with both English and Hinglish master versions.
"""
import json

with open('prompts_data.json', 'r', encoding='utf-8') as f:
    base_prompts = json.load(f)

# Helper to generate natural Hinglish prompt from English prompt
def make_hinglish(p):
    cat = p.get('category', '')
    title = p.get('title', '')
    desc = p.get('description', '')
    
    return (
        f"Act as an experienced Indian Airbnb & homestay growth consultant. "
        f"Meri property [property type] hai jo [location] me situated hai. "
        f"Guest target segment: [target guests]. "
        f"Standout verified amenities: [amenities]. "
        f"Mera host name: [host name].\n\n"
        f"Task: {title} ({desc}).\n\n"
        f"Requirements:\n"
        f"1. Tone warm, hospitable aur culturally natural Indian English / Hinglish me rakhein jo Indian travellers aur foreign guests dono ko appeal kare.\n"
        f"2. Fake promises, exaggerated distances ya imaginary amenities bilkul add mat karna. Jo details maine di hain unhi par focus karein.\n"
        f"3. Practical benefits highlight karo: sleeping comfort, hygiene, power backup, Wi-Fi speed, aur local experience.\n"
        f"4. Output me clear formatting (bullet points, scene-by-scene script, ya scannable sections) provide karein taaki seedha use kiya ja sake.\n"
        f"5. Ek strong call-to-action (CTA) include karein jo guest ko Airbnb listing check karne ke liye motivate kare."
    )

enhanced_prompts = []

# Enhance base prompts with Hinglish versions
for i, p in enumerate(base_prompts):
    ep = dict(p)
    ep['prompt_hinglish'] = make_hinglish(p)
    ep['tags'] = (p.get('tags', '') + ',hinglish,india').strip(',')
    enhanced_prompts.append(ep)

print(f"Enhanced {len(enhanced_prompts)} base prompts with Hinglish versions.")

# Now let's generate specialized high-detail prompts for Indian Homestay niches
niches = [
    {
        "cat": "Reels & Short Videos",
        "sub": "Mountain Homestay",
        "title": "Chai on the Balcony Morning Reel Script",
        "desc": "Capture the irresistible morning misty mountain vibe.",
        "en": "Write a 20-second vertical Reel script capturing the ultimate mountain morning at [property type] in [location]. Shot 1: Pouring steaming hot chai into an earthenware kulhad on the balcony with mist drifting over pine trees. Shot 2: Snuggling in a warm duvet with a book. Shot 3: Panoramic view of the snow/green peaks. Hook: 'POV: You swapped traffic horns for birds chirping at 7 AM.' Provide exact audio suggestion, on-screen text, caption, and 5 hashtags for Indian road-trippers.",
        "hi": "Mere [property type] stay jo [location] me hai, uske liye ek 20-second ki viral morning Reel script banao. Scene 1: Balcony par steaming hot chai pour karna jab piche pahadon par dhund (mist) chhayi ho. Scene 2: Cozy warm blanket me relax karna. Scene 3: Breathtaking mountain view. Hook: 'POV: City ke pollution aur traffic ko chhod kar subah 7 baje yahan aankh khuli.' Trending lo-fi audio recommendation, on-screen captions, aur high-converting caption draft provide karein.",
        "tags": "reels,mountain,morning,chai,hinglish,video"
    },
    {
        "cat": "Reels & Short Videos",
        "sub": "Goa & Beach Villa",
        "title": "Private Pool Golden Hour Reel Script",
        "desc": "Showcase luxury pool vibes for couples and small groups.",
        "en": "Create a high-energy 25-second Reel script for a private pool [property type] in [location]. Flow: Sun dipping into the horizon, water ripples reflecting golden light, a mocktail or coconut on the poolside lounger, and a group laughing by the barbecue setup. Hook: 'Why share a crowded hotel pool when you can have this entire villa to yourself?' Include upbeat tropical house audio direction, shot sequence, and a direct CTA to book via Airbnb.",
        "hi": "Mere private pool [property type] in [location] ke liye 25-second ka golden hour Reel plan banao. Visuals: Sunset ke time private pool me golden light, poolside loungers par fresh coconut water/drinks, aur cozy evening lighting. Hook: 'Hotel ke crowded pool me kyun jaana jab poora private pool villa aapka ho sakta hai?' Upbeat chill music cue, shot list, aur Airbnb link-in-bio CTA provide karein.",
        "tags": "reels,pool,villa,goa,luxury,hinglish"
    },
    {
        "cat": "Listing Optimization",
        "sub": "Workation Stays",
        "title": "High-Trust Workation Description Blueprint",
        "desc": "Convince remote workers that your Wi-Fi and power are 100% reliable.",
        "en": "Draft an authoritative, trustworthy Airbnb description section specifically targeting remote workers and tech professionals for my [property type] in [location]. Address the top 4 workation fears: 1) Verified Wi-Fi speed (mention [amenities]), 2) Inverter/generator power backup during outages, 3) Ergonomic seating and desk setup, 4) Quiet background during Zoom calls. Write in clean, professional Indian English without fluff. Include a ready-to-paste Wi-Fi speed guarantee badge format.",
        "hi": "Mere [property type] in [location] ke liye ek workation-focused Airbnb listing description likho jo IT professionals aur remote workers ko convert kare. Unke 4 main doubts clear karo: 1) Tested high-speed Wi-Fi speed test proof, 2) Power cut ke time inverter/generator backup, 3) Dedicated desk aur comfortable chair, 4) Zoom calls ke liye silent environment. Tone professional aur transparent rakhein.",
        "tags": "workation,wifi,remote work,listing,hinglish"
    },
    {
        "cat": "Guest Communication",
        "sub": "Indian Hosting Realities",
        "title": "Sudden Power Cut & Inverter Protocol",
        "desc": "De-escalate power outage anxiety with proactive communication.",
        "en": "Draft a calm, reassuring 3-step guest communication workflow for an unexpected power outage at our [property type] in [location]. 1) Immediate WhatsApp alert explaining that inverter backup is active for lights, fans, and Wi-Fi. 2) Realistic estimated restoration time from the local electricity board. 3) Caretaker assistance offer (emergency candles, phone charging station). Tone must be genuinely caring, preventing negative reviews before they happen.",
        "hi": "Area me sudden electricity power cut hone par guests ke liye ek proactive aur calm WhatsApp message draft karo. Clear karein ki inverter backup se lights, fans aur Wi-Fi chal rahe hain, heavy load (AC/geyser) power aate hi resume honge. Local electricity board ka approximate time batayein aur caretaker help offer karein taaki guest panic na kare aur negative review se bacha ja sake.",
        "tags": "guest communication,power cut,inverter,whatsapp,hinglish"
    },
    {
        "cat": "Indian Festivals & Long Weekends",
        "sub": "Diwali & Festive Stays",
        "title": "Diwali Family Getaway Campaign Kit",
        "desc": "Fill festival dates at peak ADR with family-focused marketing.",
        "en": "Develop a complete marketing campaign kit for Diwali festive holidays for our [property type] in [location]. Include: 1) Instagram announcement post celebrating pollution-free, peaceful Diwali away from city smog. 2) Family bonding highlights (open terrace for diyas, traditional sweets on arrival, private dinner setup). 3) 3-night minimum stay policy wording that guests gladly accept. 4) Canva poster copy with festive warm gold accents.",
        "hi": "Diwali long-weekend ke liye hamare [property type] in [location] ka complete festive marketing campaign plan banao. City ke pollution aur shor se door peaceful, green Diwali celebrate karne ka angle highlight karo. Family bonding, traditional welcome, terrace par diya lighting setup, aur minimum 3 nights stay policy ka respectful copy draft provide karein.",
        "tags": "festivals,diwali,campaign,poster,hinglish"
    },
    {
        "cat": "Pricing & Competitor Research",
        "sub": "Revenue Management",
        "title": "Festival & Long-Weekend Surge Pricing Formula",
        "desc": "Maximize revenue ethically during peak travel dates.",
        "en": "Act as an expert revenue manager for Indian short-term rentals. Help me set optimal surge pricing for upcoming festive dates (Diwali, New Year, Independence Day long weekend) for my [property type] in [location]. My base weekday price is ₹[paste], weekend price is ₹[paste]. Calculate recommended pricing tiers (+35% to +60%), minimum length of stay rules (2 to 3 nights), non-refundable discount strategies, and how to defend the premium price with value-added perks like complimentary bonfire or breakfast.",
        "hi": "Diwali, New Year aur long weekends ke peak dates par hamare [property type] in [location] ke liye surge pricing strategy framework banao. Base weekday rate aur weekend rate ke comparison me kitna % premium charge karna chahiye (+35% se +60%), 3-night minimum stay rule kaise implement karein, aur high price ko justify karne ke liye complimentary bonfire ya welcome breakfast kaise bundle karein.",
        "tags": "pricing,surge pricing,festivals,revenue,hinglish"
    },
    {
        "cat": "Reviews & Reputation",
        "sub": "Review Engine",
        "title": "Turning an Issue Into a 5-Star Review",
        "desc": "How exceptional service recovery earns glowing feedback.",
        "en": "During their stay, guests at my [property type] in [location] experienced a minor inconvenience [e.g. water pressure issue / AC delay], which our caretaker resolved within 45 minutes. Write a heartfelt post-stay follow-up message acknowledging the bump, thanking them for their patience, and politely inviting an honest Airbnb review highlighting how quickly the team supported them.",
        "hi": "Guest ke stay ke dauran ek chhota issue hua tha jisko hamari team ne 45 minutes me solve kar diya tha. Check-out ke baad unhe bhejne ke liye ek respectful aur heartfelt WhatsApp message likho jo unke patience ke liye shukriya ada kare aur unhe Airbnb par prompt support ka 5-star review likhne ke liye politely motivate kare.",
        "tags": "reviews,service recovery,5 star,hinglish"
    },
    {
        "cat": "Property Photography",
        "sub": "Smartphone Guide",
        "title": "Balcony & View Photography Walkthrough",
        "desc": "Avoid overexposed blown-out skies and dark indoor shadows.",
        "en": "Create a step-by-step smartphone photography checklist to shoot our balcony / mountain view at [property type] in [location]. Explain how to handle extreme dynamic range (bright sunny sky outside vs shadowy room inside) using smartphone HDR, AE/AF lock, shooting during golden hour (7–8 AM or 5–6 PM), and staging the table with two cups of chai and fresh flowers. Ensure the photo looks 100% natural and true to life.",
        "hi": "Smartphone se balcony aur window mountain view shoot karne ka step-by-step guide banao. Bahar bright dhoop aur andar shadow hone par phone ke HDR aur exposure lock ka use kaise karein, golden hour me kaise shoot karein, aur table par do cup chai stage karke natural aesthetic photo kaise lein jo reality se bilkul match kare.",
        "tags": "photography,balcony,smartphone,staging,hinglish"
    }
]

# Add more variations to reach a very rich set
destinations = [
    ("Manali, Himachal Pradesh", "Mountain Homestay / Wood Cabin", "Pahadi hospitality, snow view, bonfire, 100 Mbps Wi-Fi"),
    ("Goa (North & South)", "Beach Villa / Portuguese Heritage Home", "Private plunge pool, sunset terrace, scooter rental, beaches"),
    ("Jaipur / Udaipur, Rajasthan", "Heritage Haveli / Royal Suite", "Jharokhas, courtyards, traditional thali, cultural walking tours"),
    ("Coorg / Chikmagalur, Karnataka", "Coffee Plantation Estate", "Lush coffee trails, homemade Kodava food, birdwatching, campfire"),
    ("Lonavala / Alibaug, Maharashtra", "Weekend Farmhouse with Lawn", "BBQ grill, private swimming pool, family games, 2-hr drive from Mumbai"),
    ("Rishikesh, Uttarakhand", "Riverside Yoga & Wellness Retreat", "Ganga river view, meditation nook, organic vegetarian meals, rafting"),
    ("Munnar / Wayanad, Kerala", "Tea Garden Cottage", "Misty tea estate walks, spice plantation visits, traditional Kerala breakfast"),
    ("Gurugram / South Delhi", "Modern City Studio / Penthouse", "High-speed optical fiber, metro proximity, self-check-in, ergonomic chair")
]

counter = 133
for dest, ptype, amens in destinations:
    # Reel prompt
    enhanced_prompts.append({
        "id": f"HM{counter:03d}",
        "category": "Reels & Short Videos",
        "title": f"Viral 15s Aesthetic Reel: {ptype.split('/')[0].strip()} in {dest.split(',')[0]}",
        "description": f"High-retention short Reel template tailored for {dest}.",
        "prompt": f"Write a high-converting 15-second Instagram Reel script for a {ptype} in {dest}.Standout features: {amens}. Visual breakdown: 3-second hook with unexpected visual, 8-second rapid room & view transitions, 4-second CTA with Airbnb logo and caption instruction. Tone: aspirational yet authentic Indian travel.",
        "prompt_hinglish": f"Mere {ptype} stay jo {dest} me sthit hai, uske liye 15-second ka viral Instagram Reel script likhein. Standout amenities: {amens}. Scene 1 (0-3s): Catchy visual hook. Scene 2 (3-11s): Fast aesthetic cuts of rooms, views, and comforts. Scene 3 (11-15s): Strong booking CTA for Airbnb link in bio. Conversational Hinglish me likhein.",
        "tags": f"reels,video,viral,{dest.split(',')[0].lower().strip()},hinglish"
    })
    counter += 1

    # Listing Title prompt
    enhanced_prompts.append({
        "id": f"HM{counter:03d}",
        "category": "Listing Optimization",
        "title": f"20 Top-Ranking Listing Titles for {dest.split(',')[0]}",
        "description": f"Mobile-scannable, high-CTR titles for {ptype}.",
        "prompt": f"Generate 20 high-converting Airbnb listing titles for this {ptype} in {dest}. Key highlights: {amens}. Group into: 1) Distance & Location-led, 2) Amenity-led (Wi-Fi, pool, view), 3) Experience-led (Pahadi breakfast, peace, nature), 4) Target-audience led (couples, families, workation). Keep all titles under 50 characters so they never get cut off on mobile screens.",
        "prompt_hinglish": f"Mere {dest} sthit {ptype} ke liye 20 high-click Airbnb listing titles generate karein. Features: {amens}. Titles ko 4 categories me divide karein: Location-based, Amenity-based, Experience-based, aur Audience-based. Sabhi titles mobile screen friendly hon aur 50 characters ke andar fit hon.",
        "tags": f"titles,listing,seo,{dest.split(',')[0].lower().strip()},hinglish"
    })
    counter += 1

    # Instagram Carousel
    enhanced_prompts.append({
        "id": f"HM{counter:03d}",
        "category": "Carousel Posts",
        "title": f"7-Slide Local Insider Guide Carousel for {dest.split(',')[0]}",
        "description": f"Establish local authority with hidden gems near your stay.",
        "prompt": f"Create a 7-slide educational Instagram carousel outline: 'Secret Local Spots in {dest} Most Tourists Miss'. Slide 1: Catchy cover with stay photo. Slides 2-5: Hidden cafes, scenic walks, authentic local food, and sunset viewpoints within 15 minutes of {ptype}. Slide 6: Important travel tip (weather, roads, timings). Slide 7: 'Stay with us at [Property Name] — tap link in bio to book your stay!'",
        "prompt_hinglish": f"{dest} me hamare {ptype} ke aas-paas ke hidden gems par 7-slide ka Instagram carousel content outline banao: 'Things Most Tourists Miss in {dest.split(',')[0]}'. Local food, sunrise/sunset point, safe travel advice, aur hamare homestay me rukne ka invitation include karein.",
        "tags": f"carousel,local guide,instagram,{dest.split(',')[0].lower().strip()},hinglish"
    })
    counter += 1

    # House Rules
    enhanced_prompts.append({
        "id": f"HM{counter:03d}",
        "category": "Welcome Books & Rules",
        "title": f"Warm Yet Firm House Rules for {ptype.split('/')[0].strip()}",
        "description": f"Clear policies on quiet hours, visitors, and eco-friendly practices.",
        "prompt": f"Write a one-page house rules document for a {ptype} in {dest}. Highlights: {amens}. Address: quiet hours (10:30 PM), outside visitor restrictions, waste management/eco-friendliness, smoking policies, and pet rules if applicable. The tone must sound warm, respectful, and hospitable — not like a strict warden. Provide both English and Hinglish versions.",
        "prompt_hinglish": f"Hamare {dest} wale {ptype} ke liye warm aur clear house rules draft karein. Quiet hours, outside visitors policy, smoking area, aur electricity/water conservation ko polite and respectful tone me samjhayein taaki guest cooperate kare bina bura maane.",
        "tags": f"house rules,guest,welcome,policy,{dest.split(',')[0].lower().strip()},hinglish"
    })
    counter += 1

# Add remaining specialized niches
for item in niches:
    enhanced_prompts.append({
        "id": f"HM{counter:03d}",
        "category": item["cat"],
        "title": item["title"],
        "description": item["desc"],
        "prompt": item["en"],
        "prompt_hinglish": item["hi"],
        "tags": item["tags"]
    })
    counter += 1

print(f"Total Enhanced Prompts: {len(enhanced_prompts)}")

with open('prompts_data_enhanced.json', 'w', encoding='utf-8') as out:
    json.dump(enhanced_prompts, out, indent=2, ensure_ascii=False)

print("Saved prompts_data_enhanced.json successfully.")

