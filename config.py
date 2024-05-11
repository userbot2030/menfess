import os

api_id = int(os.environ.get("API_ID", "26477680"))
api_hash = os.environ.get("API_HASH", "b0d8504752cc1ecf52009ece2bdef0b8")
bot_token = os.environ.get("BOT_TOKEN", "6917853605:AAGicrlrxQ87KAjQol1H-UjlUkWNgtd5ymk")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://TestBoTDB:ZBfyH8EuYvxyP584@testbotdb.4srzmxk.mongodb.net/?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "wildanmenfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1002051332043"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1002068821846"))
channel_3 = int(os.environ.get("CHANNEL_3", "-1002000333870"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1002075430848"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "5779185981"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#NoyGirl #DanBoy #DanAsk #DanFind #DanSpill #DanStory #DanTalent").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph//file/89fc7945f8e5fc670bc33.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph//file/89fc7945f8e5fc670bc33.jpg")
pic_talentgirl = os.environ.get("PIC_TALENTGIRL", "https://telegra.ph//file/89fc7945f8e5fc670bc33.jpg")
pic_daddysugar = os.environ.get("PIC_DADDYSUGAR", "https://telegra.ph//file/89fc7945f8e5fc670bc33.jpg")
pic_moansgirl = os.environ.get("PIC_MOANSGIRL" , "https://telegra.ph//file/89fc7945f8e5fc670bc33.jpg")
pic_moansboy = os.environ.get("PIC_MOANSBOY" , "https://telegra.ph//file/89fc7945f8e5fc670bc33.jpg")
pic_gfrent = os.environ.get("PIC_GFRENT" , "https://telegra.ph//file/89fc7945f8e5fc670bc33.jpg")
pic_bfrent = os.environ.get("PIC_BFRENT" , "https://telegra.ph//file/89fc7945f8e5fc670bc33.jpg")
pic_owner = os.environ.get("PIC_OWNER" , "https://telegra.ph//file/1d40c754d0231d1e3e114.jpg")
pic_dan = os.environ.get("PIC_DAN" , "https://telegra.ph//file/1d40c754d0231d1e3e114.jpg")
pic_admingirl = os.environ.get("PIC_ADMINGIRL" , "https://telegra.ph//file/89fc7945f8e5fc670bc33.jpg")
pic_adminboy = os.environ.get("PIC_ADMINBOY" , "https://telegra.ph//file/1d40c754d0231d1e3e114.jpg")
# ============================================================#
pic_danboy = os.environ.get("PIC_DANBOY", "https://telegra.ph//file/1d40c754d0231d1e3e114.jpg")

# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", """"
{mention},Silahkan gunakan hastag:

#DanBoy / #NekoGirl untuk Mencari Pasangan,Teman , Partner dll
#DanAsk untuk Bertanya
#DanStory untuk Berbagi Cerita
#DanSpill untuk Spill Masalah
#NoyFind untuk Mencari Pasangan, Teman, Partner dll

{fullname} 🌱\n\nIni adalah bot menfess, semua pesan yang kamu kirim akan masuk ke channel secara anonymous. ketik /help""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim silahkan gunakan hastag:

#DanBoy / #NekoGirl untuk Mencari Pasangan, Teman , Partner dll
#DanAsk untuk Bertanya
#DanStory untuk Berbagi Cerita
#DanSpill untuk Spill Masalah
#NoyFind untuk Mencari Pasangan, Teman, Partner dll
""")
