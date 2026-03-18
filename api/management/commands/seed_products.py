from django.core.management.base import BaseCommand
from api.models import Category, Product


class Command(BaseCommand):
    help = 'Seed initial products'

    def handle(self, *args, **kwargs):
        if Product.objects.exists():
            self.stdout.write('Products already exist, skipping.')
            return
        if Category.objects.exists():
            Category.objects.all().delete()

        sweaters  = Category.objects.create(name='Sweaters',   slug='sweaters')
        chocs     = Category.objects.create(name='Chocolates', slug='chocolates')
        shawls    = Category.objects.create(name='Shawls',     slug='shawls')
        perfumes  = Category.objects.create(name='Perfumes',   slug='perfumes')
        caps      = Category.objects.create(name='Caps',       slug='caps')
        tea       = Category.objects.create(name='Tea',        slug='tea')

        sweater_data = [
            ('Floral Cable Knit', 1850, 'Bestseller', 'in', 'Ladies', 'https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=500&q=80', ['Ivory White','Dusty Rose','Blush','Mauve'], ['XS','S','M','L','XL']),
            ('Oversized Turtleneck', 2200, None, 'in', 'Ladies', 'https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=500&q=80', ['Jet Black','Wine Red','Navy Blue','Charcoal','Cream'], ['S','M','L','XL','XXL']),
            ('Ribbed Longline Cardigan', 2400, 'Low Stock', 'lo', 'Ladies', 'https://images.unsplash.com/photo-1544022613-e87ca75a784a?w=500&q=80', ['Camel Tan','Forest Green','Slate Gray','Cream'], ['S','M','L','XL']),
            ('Nordic Fair Isle', 2100, 'New', 'in', 'Ladies', 'https://images.unsplash.com/photo-1483985988355-763728e1935b?w=500&q=80', ['Ivory White','Navy Blue','Wine Red'], ['S','M','L','XL']),
            ('Merino Wool Luxury', 4500, 'Premium', 'in', 'Premium', 'https://images.unsplash.com/photo-1614093302611-8efc4f438572?w=500&q=80', ['Jet Black','Charcoal','Midnight','Ivory White'], ['S','M','L','XL','XXL']),
            ('Cashmere Turtleneck', 5200, 'Cashmere', 'lo', 'Premium', 'https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=500&q=80', ['Camel Tan','Cream','Slate Gray','Navy Blue'], ['S','M','L','XL']),
            ('Heavyweight Hoodie', 2200, None, 'in', 'Mens', 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=500&q=80', ['Jet Black','Charcoal','Navy Blue','Forest Green'], ['S','M','L','XL','XXL','3XL']),
            ('Sherpa-Lined Full Zip', 3200, 'Popular', 'in', 'Mens', 'https://images.unsplash.com/photo-1626497764746-6dc36546b388?w=500&q=80', ['Camel Tan','Olive','Navy Blue','Rust'], ['S','M','L','XL','XXL']),
            ('Alpaca Blend Oversized', 4200, None, 'in', 'Premium', 'https://images.unsplash.com/photo-1512327428406-f85d37e635ae?w=500&q=80', ['Slate Gray','Cream','Teal'], ['S','M','L','XL']),
            ('Sherpa-Lined Pullover', 2600, None, 'in', 'Ladies', 'https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=500&q=80', ['Ivory White','Blush','Mauve'], ['S','M','L','XL','XXL']),
        ]
        for name, price, tag, avail, label, img, colors, sizes in sweater_data:
            Product.objects.create(category=sweaters, name=name, price=price, tag=tag, availability=avail, label=label, image_url=img, colors=colors, sizes=sizes, emoji='🧥')

        choc_imgs = ['https://images.unsplash.com/photo-1511381939415-e44015466834?w=500&q=80','https://images.unsplash.com/photo-1548907040-4d42bda8ad3a?w=500&q=80','https://images.unsplash.com/photo-1606312619070-d48b5c7a159c?w=500&q=80','https://images.unsplash.com/photo-1619266465172-02a857c3556d?w=500&q=80','https://images.unsplash.com/photo-1528825871115-3581a5387919?w=500&q=80','https://images.unsplash.com/photo-1481391319762-47dff72954d9?w=500&q=80','https://images.unsplash.com/photo-1517093157656-b9eccef91cb1?w=500&q=80','https://images.unsplash.com/photo-1576618148400-f54bed99fcfd?w=500&q=80']
        choc_data = [('Dark Chocolate 70%',280,'🍫','Dark'),('Milk Chocolate Classic',220,'🍬','Milk'),('Hazelnut Truffle Box',380,'🌰','Truffle'),('Salted Caramel Filled',340,'🍮','Filled'),('Almond Dark Bar',300,'🥜','Dark'),('Raspberry Ganache',360,'🫐','Ganache'),('Coffee Chocolate',290,'☕','Dark'),('Gift Assorted Box',950,'🎁','Gift'),('Pistachio Praline',400,'🫘','Praline'),('Mint Crisp Dark',250,'🌿','Dark'),('Coconut Dream',260,'🥥','Milk'),('Rose Cardamom Truffle',340,'🌹','Truffle'),('Champagne Truffle',450,'🥂','Truffle'),('Saffron Milk Chocolate',420,'🌼','Milk'),('White Chocolate Bar',240,'🤍','White'),('Orange Zest Dark',270,'🍊','Dark')]
        for i,(name,price,emoji,ptype) in enumerate(choc_data):
            Product.objects.create(category=chocs, name=name, price=price, emoji=emoji, product_type=ptype, availability='in', label='Chocolate', image_url=choc_imgs[i%len(choc_imgs)])

        shawl_data = [('Pashmina Silk Blend',3200,'Bestseller',['Dusty Rose','Ivory White','Mauve','Teal'],'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=600&q=80'),('Embroidered Kashmir Shawl',4800,'Handcrafted',['Navy Blue','Wine Red','Forest Green'],'https://images.unsplash.com/photo-1509631179647-0177331693ae?w=600&q=80'),('Wool Blend Stole',1950,None,['Camel Tan','Charcoal','Cream','Mustard'],'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=600&q=80'),('Floral Printed Dupatta',1600,'New',['Blush','Ivory White','Cobalt'],'https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=600&q=80')]
        for name,price,tag,colors,img in shawl_data:
            Product.objects.create(category=shawls, name=name, price=price, tag=tag, colors=colors, availability='in', label='Shawl', image_url=img, emoji='🌿')

        perf_data = [('Mountain Mist EDP',2800,'Signature','50ml','Cedar · Vetiver · Musk','https://images.unsplash.com/photo-1541643600914-78b084683702?w=500&q=80'),('Nilgiri Bloom Attar',1850,None,'10ml','Rose · Jasmine · Sandalwood','https://images.unsplash.com/photo-1594736797933-d0401ba2fe65?w=500&q=80'),('Cozy Winter Cologne',2200,'Popular','100ml','Vanilla · Amber · Patchouli','https://images.unsplash.com/photo-1563170351-be82bc888aa4?w=500&q=80'),('Ooty Garden EDT',3200,'Limited','75ml','Green Tea · Bergamot · White Musk','https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?w=500&q=80')]
        for name,price,tag,vol,notes,img in perf_data:
            Product.objects.create(category=perfumes, name=name, price=price, tag=tag, volume=vol, notes=notes, availability='in', label='Perfume', image_url=img, emoji='🌸')

        cap_data = [('Classic Woolen Beanie',380,None,'in',['Jet Black','Navy Blue','Wine Red','Forest Green'],['Free Size'],'https://images.unsplash.com/photo-1576871337632-b9aef4c17ab9?w=400&q=80'),('Pom-Pom Knit Hat',450,None,'in',['Ivory White','Blush','Wine Red','Mustard'],['Free Size'],'https://images.unsplash.com/photo-1609803384069-19f3f58e4d7a?w=400&q=80'),('Fleece-Lined Ear Cap',520,None,'in',['Jet Black','Charcoal','Camel Tan'],['Free Size','Kids'],'https://images.unsplash.com/photo-1529231024920-9d27cf93d6c8?w=400&q=80'),('Sherpa Ushanka Cap',650,'Low Stock','lo',['Camel Tan','Cream','Slate Gray'],['Free Size'],'https://images.unsplash.com/photo-1510598155-b348f2fc74ce?w=400&q=80')]
        for name,price,tag,avail,colors,sizes,img in cap_data:
            Product.objects.create(category=caps, name=name, price=price, tag=tag, availability=avail, colors=colors, sizes=sizes, label='Cap', image_url=img, emoji='🎩')

        tea_data = [('Nilgiri Premium CTC',320,'Bestseller','250g','CTC','https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=500&q=80'),('Ooty Special Green Tea',480,'Organic','100g','Green','https://images.unsplash.com/photo-1563911892437-1feda0179e1b?w=500&q=80'),('Masala Chai Blend',280,None,'200g','Masala','https://images.unsplash.com/photo-1571934811356-5cc061b6821f?w=500&q=80'),('Earl Grey Reserve',560,'Premium','100g','Earl Grey','https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?w=500&q=80')]
        for name,price,tag,weight,ptype,img in tea_data:
            Product.objects.create(category=tea, name=name, price=price, tag=tag, weight=weight, product_type=ptype, availability='in', label='Tea', image_url=img, emoji='🍵')

        total = Product.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Seeded {total} products successfully!'))
