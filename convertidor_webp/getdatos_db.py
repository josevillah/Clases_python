import mysql.connector

def connect():
    try:
        db = mysql.connector.connect(   
            host='localhost', 
            user= 'josevillah', 
            passwd='leticia1994', 
            db='isaflor'
        )
        print('Conectado')
        return db
    except:
        print('Error trying to connect to database!!')
    
def png_y_jpg_to_webp():
    db = connect()
    if db:
        cursor = db.cursor()
        sql = "SELECT id, urlimagen FROM productos" 
        cursor.execute(sql)
        productos = cursor.fetchall()

        for pro in productos:
            id = pro[0]
            if '.png' in pro[1]:
                name = pro[1].replace('.png', '.webp')
            elif '.jpg' in pro[1]:
                name = pro[1].replace('.jpg', '.webp')
            elif '.jpeg' in pro[1]:
                name = pro[1].replace('.jpeg', '.webp')
            sql = "UPDATE productos SET urlimagen = %s WHERE id = %s"
            values = (name,id)
            cur = db.cursor()
            cur.execute(sql, values)
            db.commit()
        print('Proceso Terminado')

def publicidad_to_webp():
    db = connect()
    if db:
        cursor = db.cursor()
        sql = "SELECT id, url FROM pubenlaces" 
        cursor.execute(sql)
        publicidades = cursor.fetchall()
        for p in publicidades:
            id = p[0]
            if '.png' in p[1]:
                name = p[1].replace('.png', '.webp')
            elif '.jpg' in p[1]:
                name = p[1].replace('.jpg', '.webp')
            sql = "UPDATE pubenlaces SET url = %s WHERE id = %s"
            values = (name,id)
            cur = db.cursor()
            cur.execute(sql, values)
            db.commit()
        print('Proceso Terminado')

def banners_to_webp():
    db = connect()
    if db:
        cursor = db.cursor()
        sql = "SELECT id, url FROM banners" 
        cursor.execute(sql)
        publicidades = cursor.fetchall()
        for p in publicidades:
            id = p[0]
            if '.png' in p[1]:
                name = p[1].replace('.png', '.webp')
            elif '.jpg' in p[1]:
                name = p[1].replace('.jpg', '.webp')
            sql = "UPDATE banners SET url = %s WHERE id = %s"
            values = (name,id)
            cur = db.cursor()
            cur.execute(sql, values)
            db.commit()
        print('Proceso Terminado')
            

banners_to_webp()