from pymongo import MongoClient


MONGO_URI = "mongodb+srv://conectt:conectt234@cluster0.vvjkhyp.mongodb.net/freshpetals?appName=Cluster0"
client = MongoClient(MONGO_URI)

db = client["freshpetals"]
products_collection = db["products"]

products_collection.delete_many({})

products = [
    # ---------------- ROSES ----------------
    {
        "name": "Blush Pink Rose Bouquet",
        "description": "Soft pink roses wrapped in pastel paper, perfect for saying thank you or sorry.",
        "price": 259,
        "stock": 24,
        "category": "Roses",
        "images": ["https://gulmahal.in/wp-content/uploads/2024/09/DSC_3061-Photoroom.jpg"],
    },
     {
        "name": "Spring Pastel Tulip Bunch",
        "description": "Mixed pastel tulips that bring fresh spring energy to any room.",
        "price": 799,
        "stock": 40,
        "category": "Tulips",
        "images": ["https://lepastelribbon.com/cdn/shop/files/4E3F854B-C43A-4741-92CD-D6E10E78C7EE.jpg?v=17181282426"],
    },
     {
    "name": "Yellow Friendship Roses",
    "description": "Bright yellow roses that represent friendship, joy, and positivity.",
    "price": 249,
    "stock": 26,
    "category": "Roses",
    "images": ["https://www.juneflowers.com/wp-content/uploads/2025/08/Midnight-Sunshine-Black-Yellow-Rose-Bouquet.png"],
     },
      {
    "name": "Sunflower and Lily Bouquet",
    "description": "Elegant bouquet combining bright sunflowers with fresh white lilies.",
    "price": 499,
    "stock": 12,
    "category": "Mixed Bouquets",
    "images": ["https://arpanflowers.com/wp-content/uploads/2025/12/IMG2025122614363728129.jpg"],
   },
    {
        "name": "Classic Red Rose Dozen",
        "description": "12 long‑stem red roses with seasonal fillers for pure romance.",
        "price": 399,
        "stock": 32,
        "category": "Roses",
        "images": ["https://static-assets-prod.fnp.com/images/pr/l/v20231117183645/forever-yours-red-rose-bouquet_1.jpg"],
    },
    
    {
    "name": "Crochet Sunflower Bouquet",
    "description": "Bright crochet sunflowers carefully handmade with soft yarn for a cheerful gift.",
    "price": 139,
    "stock": 18,
    "category": "Crochet Flowers",
    "images": ["https://cdn.vibecity.in/providers/63ef91705b73b600173fbb46/1000042162_34a77209-0320-4c04-a851-4b3c8b103d71-3X.png"],
    },
    {
        "name": "Sunset Peach Rose Box",
        "description": "Luxury peach rose box that feels warm and cozy, great for anniversaries.",
        "price": 399,
        "stock": 16,
        "category": "Roses",
        "images": ["https://ovenfresh2025.s3.eu-north-1.amazonaws.com/New_Website_products/2023/02/Peach-Roses-With-Baby-Breath-In-A-Box_1-min.jpg"],
    }, 
     {
    "name": "White Rose Elegance",
    "description": "Beautiful white roses symbolizing purity and peace, perfect for weddings and special occasions.",
    "price": 299,
    "stock": 20,
    "category": "Roses",
    "images": ["https://m.media-amazon.com/images/I/61a-H+BlEfL._AC_UF894,1000_QL80_.jpg"],
    },
    {
        "name": " Sunflower Hand Bunch",
        "description": "Tall sunflowers tied with rustic jute, full of positive vibes.",
        "price": 599,
        "stock": 36,
        "category": "Sunflowers",
        "images": ["https://www.juneflowers.com/wp-content/uploads/2022/09/sunflower_bouquet.png"],
    },
    {
    "name": "Heart Shape Rose Arrangement",
    "description": "Heart-shaped arrangement of red roses designed for romantic surprises.",
    "price": 499,
    "stock": 8,
    "category": "Roses",
    "images": ["https://cdn.flowersnfruits.com/uploads/product/flowers_n_fruits/1687421455_13145.png"],
    },
    {
    "name": "Rose and Baby Breath Bouquet",
    "description": "Fresh red roses combined with delicate baby breath flowers for an elegant look.",
    "price": 59,
    "stock": 14,
    "category": "Roses",
    "images": ["https://jm.com.sg/cdn/shop/files/59.png?v=1717253010&width=1214"],
   },
    {
    "name": "Mixed Color Rose Bouquet",
    "description": "A stunning bouquet of red, pink, yellow, and white roses for joyful moments.",
    "price": 349,
    "stock": 17,
    "category": "Mixed Bouquets",
    "images": ["https://floweronwheels.com/cdn/shop/products/19.jpg?v=1667240802"],
    },


    # ---------------- TULIPS ----------------
   
    {
    "name": "White Tulip Elegance",
    "description": "Elegant white tulips arranged in a stylish bouquet for weddings and formal occasions.",
    "price": 799,
    "stock": 14,
    "category": "Tulips",
    "images": ["https://studioinflorescence.com/cdn/shop/files/Pure_White_Tulips_Fresh_Dutch_Tulip_Bouquet_by_the_Bunch.jpg?v=1764076090&width=1946"],
     },
     {
    "name": "Purple Tulip Royal Bouquet",
    "description": "Luxury bouquet of purple tulips representing elegance and royalty.",
    "price": 949,
    "stock": 12,
    "category": "Tulips",
    "images": ["https://media.istockphoto.com/id/468329084/photo/purple-tulips-bouquet.jpg?s=612x612&w=0&k=20&c=9dUmwSSWIsEUZ37wHUjpyKp3lHlTCyjcEyK-1h5Ev6A="],
     },
      {
    "name": "Festival Mixed Flower Basket",
    "description": "A decorative basket filled with colorful seasonal flowers for festive gifting.",
    "price": 1099,
    "stock": 12,
    "category": "Mixed Bouquets",
    "images": ["https://cdn.bloomsflora.com/uploads/product/flowers_n_fruits/OCT2024/1728454090079-MixedRosesinaBasket.webp"],
    },

    {
        "name": "Yellow Tulips",
        "description": "Bright yellow tulips that feel like a sunny morning in a vase.",
        "price": 899,
        "stock": 28,
        "category": "Tulips",
        "images": ["https://www.vanrina.com/cdn/shop/products/yellow_tulip_2_2000x2000.jpg?v=1615094064"],
    },
    {
        "name": " Red Tulip Wrap",
        "description": "Deep red tulips wrapped with baby’s breath, made for date nights.",
        "price": 899,
        "stock": 22,
        "category": "Tulips",
        "images": ["https://blacktulipflowers.in/wp-content/uploads/2024/01/Unchained-Melody.png"],
    },
    # ---------------- LILIES ----------------
    {
        "name": "Pure White Lily Bouquet",
        "description": "Fragrant white lilies that bring calm and peace to celebrations.",
        "price": 499,
        "stock": 20,
        "category": "Lilies",
        "images": ["https://samuiflowers.com/wp-content/uploads/2021/01/White-Lilies-in-Black-Wrap.jpg"],
    },
    {
    "name": "Orange Lily Bright Bouquet",
    "description": "Bright orange lilies that symbolize passion and energy.",
    "price": 579,
    "stock": 11,
    "category": "Lilies",
    "images": ["https://i.pinimg.com/736x/ba/22/e1/ba22e134d89ed06618a768b953646053.jpg"],
    },
   
    {
    "name": "Lily and Rose Mixed Bouquet",
    "description": "Elegant combination of lilies and roses for a premium gift arrangement.",
    "price": 1099,
    "stock": 10,
    "category": "Mixed Bouquets",
    "images": ["https://floweronwheels.com/cdn/shop/products/s-surprize.jpg?v=1662406747"],
    },

    {
    "name": "Luxury Lily Flower Basket",
    "description": "Premium arrangement of fresh lilies in a decorative basket for celebrations.",
    "price": 499,
    "stock": 12,
    "category": "Lilies",
    "category": "Mixed Bouquets",
    "images": ["https://www.floweree.in/cdn/shop/files/Gemini_Generated_Image_chrrdhchrrdhchrr_large.png?v=1767979624"],
    },
    {
    "name": "White Lily and Green Filler Bouquet",
    "description": "Classic bouquet of white lilies combined with fresh green fillers.",
    "price": 699,
    "stock": 16,
    "category": "Lilies",
    "images": ["https://sweetheartflorist.com.au/cdn/shop/products/image_faa94689-83fa-4392-91cb-6dd9516f3f6e.jpg?v=1626938632"],
},
    {
        "name": "Pink Lily ",
        "description": "Soft pink lilies arranged in a clear glass vase for living rooms.",
        "price": 199,
        "stock": 18,
        "category": "Lilies",
        "images": ["https://nestasia.in/cdn/shop/products/DSC_2570.jpg?v=1675768965"],
    },
    {
        "name": "White & Pink Lily Mix",
        "description": "A soothing mix of white and blush lilies, ideal for get‑well wishes.",
        "price": 899,
        "stock": 14,
        "category": "Lilies",
        "images": ["https://www.flowerzila.com/wp-content/uploads/2021/11/17-min.jpg"],
    },
    #-----------------Gerbera-------------------
    {
"name": "yellow Gerbera",
"description": "Beautiful colorful gerbera flowers commonly used in bouquets and floral arrangements.",
"price": 145,
"stock": 50,
"category": "Gerbera",
"images": ["https://www.sunstrums.ca/cdn/shop/products/Studio_Session-2822_1024x1024.jpg?v=1731964781"]
},
  {
"name": "orange Gerbera",
"description": "Beautiful colorful gerbera flowers commonly used in bouquets and floral arrangements.",
"price": 200,
"stock": 50,
"category": "Gerbera",
"images": ["https://www.shutterstock.com/image-photo/still-life-orange-gerberas-daisies-260nw-2694930831.jpg"]
},  
{
"name": "red Gerbera",
"description": "Beautiful colorful gerbera flowers commonly used in bouquets and floral arrangements.",
"price":165 ,
"stock": 50,
"category": "Gerbera",
"images": ["https://img.freepik.com/premium-photo/gerbera-daisy-flowers-glass-jar-white-wall-background_154515-3616.jpg"]
},  
{
"name": "mix Gerbera",
"description": "Beautiful colorful gerbera flowers commonly used in bouquets and floral arrangements.",
"price": 245,
"stock": 50,
"category": "Gerbera",
"images": ["https://www.fnp.com/images/pr/l/v20240711174941/brilliant-gerbera-mix_1.jpg"]
},
 {
"name": "white Gerbera",
"description": "Beautiful colorful gerbera flowers commonly used in bouquets and floral arrangements.",
"price": 95,
"stock": 50,
"category": "Gerbera",
"images": ["https://ovenfresh2025.s3.eu-north-1.amazonaws.com/New_Website_products/2023/02/Vase-Of-White-Gerberas_1.jpg"]
},
{
"name": "pink Gerbera",
"description": "Beautiful colorful gerbera flowers commonly used in bouquets and floral arrangements.",
"price": 95,
"stock": 50,
"category": "Gerbera",
"images": ["https://sagarflorist.com/wp-content/uploads/2024/08/jaewera.png"]
},
    # ---------------- SUNFLOWERS ----------------
    
    {
    "name": "Sunflower Celebration Basket",
    "description": "Decorative basket arrangement of fresh sunflowers perfect for celebrations.",
    "price": 499,
    "stock": 14,
    "category": "Sunflowers",
    "images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgaSN8DOQURUx52zW3OKCt_uoDBRgx-gwi5g&s"],
    },
    {
    "name": "Colorful Mixed Flower Bouquet",
    "description": "A vibrant bouquet of roses, lilies, and daisies arranged beautifully for joyful occasions.",
    "price": 549,
    "stock": 18,
    "category": "Mixed Bouquets",
    "images": ["https://www.floramoments.in/cdn/shop/files/product9.png?v=1714115826"],
    },

    {
        "name": "Sunflower & Greens Vase",
        "description": "Bright sunflowers arranged with fresh greens in a reusable vase.",
        "price": 399,
        "stock": 20,
        "category": "Sunflowers",
        "images": ["https://www.petalsonprince.com/wp-content/uploads/2016/04/six-sunflowers-1-scaled.jpg"],
    },
    {
        "name": "Mini Sunflower Posy",
        "description": "Compact sunflower bunch that fits perfectly on a study table.",
        "price": 109,
        "stock": 30,
        "category": "Sunflowers",
        "images": ["https://gracefloral.in/cdn/shop/files/73B1E7AE-143F-4F98-BF82-5894FE979714.jpg?v=1728640432"],
    },
  

  # ---------------- MIXED BOUQUETS ----------------
    {
        "name": "Mixed flower Bouquet",
        "description": "A friendly mix of seasonal blooms you can gift on any day.",
        "price": 599,
        "stock": 34,
        "category": "Mixed Bouquets",
        "images": ["https://www.floweree.in/cdn/shop/files/Gemini_Generated_Image_ggbq1wggbq1wggbq_1024x1024.png?v=1766684808"],
    },
    {
        "name": "Pastel Dream Box Arrangement",
        "description": "Soft pastel flowers styled in a box that feels dreamy and gentle.",
        "price": 1999,
        "stock": 16,
        "category": "Mixed Bouquets",
        "images": ["https://assets.eflorist.com/site/EF-14903/assets/products/EZM_/skusku13781908.jpg?impolicy=hero"],
    },
    {
        "name": "Grand Celebration Bouquet",
        "description": "Tall, full bouquet with roses, lilies and fillers for big milestones.",
        "price": 799,
        "stock": 10,
        "category": "Mixed Bouquets",
        "images": ["https://static-assets-prod.fnp.com/images/pr/l/v20251219154513/rosy-orchid-celebration-bouquet_1.jpg"],
    },
    {
    "name": "Royal Blue Orchid Bouquet",
    "description": "Elegant blue orchids arranged in a stylish bouquet that feels rare and luxurious.",
    "price": 659,
    "stock": 14,
    "category": "Orchids",
    "images": ["https://florista.in/cdn/shop/files/TrueBlueOrchids.png?v=1748248188"],
    },
    {
"name": "Pink Gerbera Bouquet",
"description": "Elegant bouquet of fresh pink gerbera flowers wrapped in decorative paper for special occasions.",
"price": 349,
"stock": 20,
"category": "Mixed Bouquets",
"images": ["https://www.nillablooms.com/wp-content/uploads/2025/02/1633930244_15.webp"]
},

{
"name": "Yellow Gerbera Bouquet",
"description": "Bright yellow gerbera bouquet symbolizing happiness and friendship.",
"price": 329,
"stock": 18,
"category": "Mixed Bouquets",
"images": ["https://cdn.bloomsflora.com/uploads/product/bloomsflora/13585_86_13585.png"]
},
{
"name": "Gerbera Celebration Bouquet",
"description": "A vibrant bouquet of mixed gerbera flowers designed for celebrations, birthdays and anniversaries.",
"price": 449,
"stock": 15,
"category": "Mixed Bouquets",
"images": ["https://img.tatacliq.com/images/i30/437Wx649H/MP000000024367183_437Wx649H_202602121542441.jpeg"]
},
{
"name": "Mixed Rose Bouquet",
"description": "A beautiful bouquet of red, pink and white roses perfect for romantic gifts and special occasions.",
"price": 499,
"stock": 20,
"category": "Mixed Bouquets",
"images": ["https://cdn.giftlaya.com/images/23/b7d5225a-e7bd-4918-b7aa-92e69b33f654.webp"]
},
{
"name": "Colorful Mixed Flower Bouquet",
"description": "A vibrant bouquet containing roses, gerberas and lilies arranged beautifully for celebrations.",
"price": 549,
"stock": 18,
"category": "Mixed Bouquets",
"images": ["https://www.flowersonnortonst.com.au/cdn/shop/files/IMG_5481_1.jpg?v=1704145560&width=1946"]
},
{
"name": "Mixed Lily Bouquet",
"description": "Fresh white and pink lilies arranged in an elegant bouquet for weddings and anniversaries.",
"price": 599,
"stock": 15,
"category": "Mixed Bouquets",
"images": ["https://tilia.in/wp-content/uploads/2022/07/attractive-mixed-asiatic-lilies-bunch_41.webp"]
},
{
"name": "Premium Mixed Flower Bouquet",
"description": "A premium bouquet featuring roses, orchids, lilies and gerberas for luxury gifting.",
"price": 799,
"stock": 12,
"category": "Mixed Bouquets",
"images": ["https://flowera.in/uploads/products/mixed-flower-bouquet.jpg"]
},
{
"name": "Sunflower & Rose Mixed Bouquet",
"description": "A vibrant bouquet of bright sunflowers and romantic red roses, perfect for birthdays and joyful celebrations.",
"price": 499,
"stock": 18,
"category": "Mixed Bouquets",
"images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpobL-40nk0poDgCSU91vkj2RU7mw8cohqug&s"]
},

{
"name": "Festival Mixed Bouquet",
"description": "Colorful flowers arranged together for festivals, pooja and special occasions.",
"price": 399,
"stock": 24,
"category": "Mixed Bouquets",
"images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQw4LsJIPpFjq94M8T_14l2zvGi6gL_0d0lBg&s"]
},

    # ---------------- BIRTHDAY FLOWERS ----------------
    {
        "name": "Happy Birthday Bouquet",
        "description": "Colorful mixed flowers that feel like confetti in a bouquet.",
        "price": 399,
        "stock": 26,
        "category": "Birthday Flowers",
        "images": ["https://m.media-amazon.com/images/I/71gbUhBjWNL.jpg"],
    },
    {
        "name": "Birthday Rose & Balloon Combo",
        "description": "Classic roses paired with a cute birthday balloon for quick gifting.",
        "price": 899,
        "stock": 20,
        "category": "Birthday Flowers",
        "images": ["https://giftr.my/cdn/shop/files/861024D6-A40F-4B40-8825-58A54C636ED4_1024x1024.jpg?v=1737401826"],
    },
    {
        "name": "Birthday Flower Basket",
        "description": "Bright basket of blooms that can directly sit on the party table.",
        "price": 599,
        "stock": 18,
        "category": "Birthday Flowers",
        "images": ["https://flowera.in/uploads/tempDir/proGImg_07_66aa15de401c1-600X600.webp"],
    },

    # ----------------  Orchid FLOWERS ----------------
    {
    "name": "Purple Orchid Elegance",
    "description": "Graceful purple orchids arranged in a ceramic pot for elegant gifting.",
    "price": 499,
    "stock": 14,
    "category": "Orchids",
    "images": ["https://www.fnp.com/images/pr/l/v20240711175812/royal-purple-orchid-elegance_1.jpg"],
},
{
    "name": "White Orchid Serenity",
    "description": "Pure white orchids symbolizing peace and sophistication.",
    "price": 599,
    "stock": 18,
    "category": "Orchids",
    "images": ["https://www.chennaionlineflorists.com/uploaded/product/IND17398.webp"],
},
{
    "name": "Pink Orchid Delight",
    "description": "Soft pink orchid stems perfect for elegant home decor.",
    "price": 499,
    "stock": 12,
    "category": "Orchids",
    "images": ["https://www.bhubaneswarflowershop.com/uploaded/product/IND17649.webp"],
},
{
    "name": "Pink Orchid ",
    "description": "Soft pink orchid stems perfect for gifts .",
    "price": 699,
    "stock": 12,
    "category": "Orchids",
    "images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmDkFCKjOLty10oj9DIkhqORatfXHCf_a62w&s"],
},
# ---------------- CROCHET FLOWERS ----------------
{
    "name": "Handmade Crochet Rose Bouquet",
    "description": "Beautiful handmade crochet roses that last forever, perfect for unique gifts.",
    "price": 399,
    "stock": 20,
    "category": "Crochet Flowers",
    "images": ["https://i.etsystatic.com/41548668/r/il/09421a/6629884803/il_570xN.6629884803_8vmc.jpg"],
},

{
    "name": "Pastel Crochet Flower Bouquet",
    "description": "Soft pastel crochet flowers arranged in a cute bouquet that never fades.",
    "price": 699,
    "stock": 14,
    "category": "Crochet Flowers",
    "images": ["https://i.etsystatic.com/24994290/r/il/1ec2f0/4759958348/il_570xN.4759958348_kk9g.jpg"],
},
{
    "name": "Crochet Tulip Gift Bouquet",
    "description": "Handcrafted crochet tulips wrapped beautifully, ideal for long-lasting gifts.",
    "price": 249,
    "stock": 16,
    "category": "Crochet Flowers",
    "images": ["https://i.pinimg.com/736x/18/ce/d9/18ced9fa06e65b0326296acb9ca0e56d.jpg"],
},
{
    "name": "Luxury Crochet Flower Box",
    "description": "Premium box arrangement of handmade crochet flowers designed for special occasions.",
    "price": 999,
    "stock": 10,
    "category": "Crochet Flowers",
    "images": ["https://m.media-amazon.com/images/I/81G52+2+uxL._AC_UF894,1000_QL80_.jpg"],
},
{
    "name": "Crochet Daisy Bouquet",
    "description": "Cute handmade crochet daisies arranged in a small bouquet for charming gifts.",
    "price": 80,
    "stock": 22,
    "category": "Crochet Flowers",
    "images": ["https://therui.in/wp-content/uploads/2025/03/1000516059-scaled-1-1-640x853.jpg"],
},
{
    "name": "Rainbow Crochet Flower Bouquet",
    "description": "Colorful handmade crochet flowers designed to brighten any space.",
    "price": 699,
    "stock": 12,
    "category": "Crochet Flowers",
    "images": ["https://sc04.alicdn.com/kf/Hb868ad071d1342ffb0a3e1153094c8e9J.jpg"],
},
#----------------varmals-----------------------
  {
    "name": "Classic Rose Varmala",
    "description": "Traditional red rose varmala used in weddings.",
    "price": 699,
    "stock": 20,
    "category": "Varmala",
    "images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDXQ7wxRpTePwA_vCyB7PenKkriK7p91v8rg&s"]
  },
  
  {
    "name": "Mixed Flower Varmala",
    "description": "Colorful combination of roses, lilies, and orchids.",
    "price": 799,
    "stock": 18,
    "category": "Varmala",
    "images": ["https://vasavicrafts.com/cdn/shop/files/mogra-pink-rose-jaimala-varmala3.jpg?v=1738879170&width=1200"]
  },
  {
    "name": "Marigold Wedding Varmala",
    "description": "Traditional marigold varmala for cultural weddings.",
    "price": 499,
    "stock": 25,
    "category": "Varmala",
    "images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSo_gVpIjoAm-4dBB0tA5FN9O3rc0j_RdNSog&s"]
  },
  {
    "name": "Designer Pearl Varmala",
    "description": "Stylish varmala with flowers and pearl decorations.",
    "price": 799,
    "stock": 10,
    "category": "Varmala",
    "images": ["https://i.pinimg.com/736x/0b/b6/cc/0bb6ccffbe65346ca577e36bc55d9f90.jpg"]
  },
  {
    "name": "white and Pink Rose Varmala",
    "description": "Soft pink rose varmala for romantic wedding themes.",
    "price": 599,
    "stock": 20,
    "category": "Varmala",
    "images": ["https://arpanflowers.com/wp-content/uploads/2024/01/Pink-White-Rose-With-Babys-breath-Varmala1.png"]
  },
   {
    "name": "white rose and mogra Varmala",
    "description": "Soft white mogra varmala for romantic wedding themes.",
    "price": 599,
    "stock": 20,
    "category": "Varmala",
    "images": ["https://www.atfleurs.com/cdn/shop/files/tempImagevhYOjP.jpg?v=1772019212&width=1100"]
  },

# ---------------- Daily Flowers ----------------
{
  "name": "Marigold Flower",
  "description": "Bright yellow and orange flowers commonly used in Indian pooja, garlands and festival decorations.",
  "price": 120,
  "stock": 80,
  "category": "Daily Flowers",
  "images": ["https://cdn.shopify.com/s/files/1/0579/7924/0580/files/581d611d20_600x600.jpg?v=1729245513"]
},
{
  "name": "Jasmine (Mogra)",
  "description": "Fragrant white jasmine flowers used for hair decoration and daily temple offerings.",
  "price": 30,
  "stock": 60,
  "category": "Daily Flowers",
  "images": ["https://maayajewellery.com/wp-content/uploads/2025/11/F3.jpg"]
},
{
  "name": "Lotus Flower",
  "description": "Sacred lotus flower often used in temples and religious ceremonies.",
  "price": 30,
  "stock": 25,
  "category": "Daily Flowers",
  "images": ["https://cdn.dotpe.in/longtail/store-items/8293413/it2wmdlu.webp"]
},
{
  "name": "purple Lotus Flower",
  "description": "Sacred lotus flower often used in temples and religious ceremonies.",
  "price": 30,
  "stock": 25,
  "category": "Daily Flowers",
  "images": ["https://m.media-amazon.com/images/I/51gtCydRYAL.jpg"]
},
{
  "name": "white Lotus Flower",
  "description": "Sacred lotus flower often used in temples and religious ceremonies.",
  "price": 30,
  "stock": 25,
  "category": "Daily Flowers",
  "images": ["https://thumbs.dreamstime.com/b/close-up-top-view-white-lotus-flower-blooming-outstanding-leaf-pond-vertical-112458086.jpg"]
},

{
  "name": "yellow Hibiscus Flower",
  "description": "Red hibiscus flowers commonly offered to Lord Ganesha and Goddess Kali.",
  "price": 20,
  "stock": 40,
  "category": "Daily Flowers",
  "images": ["https://dukaan.b-cdn.net/700x700/webp/upload_file_service/33f4f304-0403-4004-96ef-bd01766a09ee/orange-hibiscus-flower-2022-11-08-08-19-44-utc.jpg"]
},
{
  "name": "Red Hibiscus Flower",
  "description": "Red hibiscus flowers commonly offered to Lord Ganesha and Goddess Kali.",
  "price": 20,
  "stock": 40,
  "category": "Daily Flowers",
  "images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZdA6dMZ9Zj2PjocZvxLA3Zx1iqYG8bmCpRQjlzjvln_RgPPS0X5zIwEeZqGHP1NkZGzM&usqp=CAU"]
},
{
"name": "Chrysanthemum",
"description": "Colorful chrysanthemum flowers widely used in garlands and festival decorations.",
"price": 40,
"stock": 55,
"category": "Daily Flowers",
"images": ["https://theflora.in/cdn/shop/products/Chrysanthemum2.jpg?v=1664724668&width=3384"]
},

{
  "name": "pink Chrysanthemum (Shevanti)",
  "description": "Popular yellow and white flowers used in temple garlands and daily decorations.",
  "price": 60,
  "stock": 45,
  "category": "Daily Flowers",
  "images": ["https://cdn.grofers.com/cdn-cgi/image/f=auto,fit=scale-down,q=70,metadata=none,w=270/da/cms-assets/cms/product/4811b6f3-927f-45e7-8999-8849af6f33df.png"]
},
{
  "name": "yellow Chrysanthemum (Shevanti)",
  "description": "Popular yellow and white flowers used in temple garlands and daily decorations.",
  "price": 60,
  "stock": 45,
  "category": "Daily Flowers",
  "images": ["https://cdn.grofers.com/cdn-cgi/image/f=auto,fit=scale-down,q=70,metadata=none,w=1080/da/cms-assets/cms/product/10704afc-c476-4fec-b627-4e36e5a064de.png"]
},

{
  "name": "mix Marigold Chrysanthemum (Shevanti)",
  "description": "Popular yellow and white flowers used in temple garlands and daily decorations.",
  "price": 60,
  "stock": 45,
  "category": "Daily Flowers",
  "images": ["https://www.phoolvale.com/newadmin/uploads/products/product_1758612119_68d24a977f999.webp"]
},
{
  "name": "white Chrysanthemum (Shevanti)",
  "description": "Popular yellow and white flowers used in temple garlands and daily decorations.",
  "price": 60,
  "stock": 45,
  "category": "Daily Flowers",
  "images": ["https://gulmahal.in/wp-content/uploads/2024/10/White-Chamanti-Flowers.webp"]
},

{
  "name": " michelia (Champa)",
  "description": "Soft fragrant temple flowers widely used in South Indian temple offerings.",
  "price": 60,
  "stock": 20,
  "category": "Daily Flowers",
  "images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRb2QnjkrnEUjm2KSLCPbY7LSo1KUcoOroSMkoE6gm1gDXq96AeGViPASOjsrc8zGthV7Y&usqp=CAU"]
},
#---------------------funeral----------------------------------
{
    "name": " Rose Funeral Bouquet",
    "description": "Elegant roses symbolizing peace and remembrance.",
    "price": 599,
    "stock": 25,
    "category": "Funeral",
    "images": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmUxYSpXnc6eVZMZlM747e3O4xA0MQ0gxe_Q&s"]
  },
  {
    "name": "Lily Sympathy Arrangement",
    "description": "White lilies arranged for expressing condolences.",
    "price": 799,
    "stock": 20,
    "category": "Funeral",
    "images": ["https://fyf.tac-cdn.net/images/products/small/V7000.jpg?auto=webp&quality=60&width=650"]
  },
    {
    "name": "Mixed Sympathy Bouquet",
    "description": "Combination of white roses, lilies, and carnations.",
    "price": 699,
    "stock": 18,
    "category": "Funeral",
    "images": ["https://thumbs.dreamstime.com/z/sympathy-wreath-near-tree-classic-sympathy-wreath-near-tree-cemetery-109200315.jpg"]
  },
  {
  "name": "Sympathy Flower Basket",
  "description": "Basket of mixed white flowers arranged for condolence gifting.",
  "price":499,
  "stock": 12,
  "category": "Funeral",
  "images": ["https://m.media-amazon.com/images/I/71+9PUy9fyS._AC_UF1000,1000_QL80_.jpg"]
},
  {
    "name": "Peaceful Orchid Stand",
    "description": "Orchid arrangement for respectful funeral ceremonies.",
    "price": 599,
    "stock": 15,
    "category": "Funeral",
    "images": ["https://www.blossomflorist.co/cdn/shop/files/22.png?v=1774140796&width=1535"]
  },
  
  {
    "name": "White Chrysanthemum Wreath",
    "description": "Traditional wreath used for funeral ceremonies.",
    "price": 299,
    "stock": 12,
    "category": "Funeral",
    "images": ["https://powersoft365customers.blob.core.windows.net/he391780-flower-works-by-marina-c-ltd/Items/FUNE-WREATHGYP.jpg"]
  },
  


]


result = products_collection.insert_many(products)

print(f"✅ {len(result.inserted_ids)} products inserted successfully!")