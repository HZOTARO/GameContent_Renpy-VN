# Declare characters used by this game. The color argument colorizes the name of the character.
define narrator = Character(what_color="#000000")
define MC = Character()
define joshua = Character("Joshua", color="#777626")
define christine = Character("Christine", color="#5000a7")
define mary = Character("Kak Mary", color="#c26e00")
define gerry = Character("Pak Gerry", color="#6f2700")
define lecturer = Character("Dosen", color="#000000")
define mahasiswa = Character("Mahasiswa", color="#000000")

define PS = 0  # Programming Skill
define DS = 0  # Design Skill
# define E = 10  # Energy

# The game starts here.
label start:
    call semester_1
    jump semester_2
    return

label semester_1:
    scene bg college outdoor with fade
    "Kamu memulai semester pertama kuliah."

    scene bg college teacherroom with dissolve
    show gerry smile
    gerry "Halo, perkenalkan nama saya Gerry. Saya yang akan menjadi dosen wali kalian sepanjang perkuliahan. Semangat kuliahnya!"

    scene bg college classroom with fade
    lecturer "Halo, perkenalkan saya yang akan mengajar kalian untuk mata kuliah Pemrograman Dasar sepanjang satu semester ini."
    lecturer "Untuk awal perkuliahan kita akan belajar mengenai variabel dan tipe data, serta operasi matematika sederhana di dalam pemrograman"
    $ PS += 1

    scene bg college hallway with dissolve
    "Setelah kelas, kamu dihadapkan pada dua pilihan"
    
    menu:            
        "Pergi ke perpustakaan":
            scene bg library big with dissolve
            "Kamu memutuskan untuk pergi ke perpustakaan untuk belajar."
            MC "(Lebih baik aku belajar lebih awal untuk memastikan aku paham materi.)"
            
            menu:
                "Belajar bahasa pemrograman":
                    $ PS += 1
                "Belajar algoritma pemrograman":
                    $ DS += 1
            "Kamu meningkatkan kemampuan pemrogramanmu."
        
        "Istirahat di rumah":
            scene bg home bedroom with dissolve
            "Kamu memutuskan untuk pulang dan beristirahat di rumah."
            MC "(Istirahat dulu agar aku punya lebih banyak energi nanti.)"
            "Kamu merasa lebih segar setelah beristirahat."

    scene bg college hallway with fade
    "Beberapa minggu berlalu, dan kamu sekarang harus menghadapi ujian."
    MC "(Aku harus lulus dengan nilai bagus!)"
    "Kamu lulus ujian dengan hasil yang memuaskan!"

    scene bg college teacherroom with fade
    show gerry smile
    "Kamu bertemu kembali dengan Pak Gerry untuk evaluasi semester."
    gerry "Bagaimana perkuliahanmu satu semester ini?"
    MC "Menurut saya baik kok Pak, aman."
    gerry "Hmm.. saya lihat nilaimu bagus. Teruskan ya."
    MC "Ok, Pak."
    
    "MC bersiap-siap untuk semester kedua."
    return

label semester_2:
    scene black with fade
    "Semester 2 dimulai."

    scene bg college classroom with fade
    show gerry smile
    gerry "Halo, perkenalkan saya yang akan mengajar kalian untuk mata kuliah Pemrograman Berorientasi Objek sepanjang satu semester ini."
    MC "(Wah.. Dosen kelas ini Pak Gerry.)"
    gerry "Untuk awal perkuliahan kita akan belajar mengenai apa itu Pemrograman Berorientasi Objek(PBO)."
    gerry "Pemrograman berbasis objek adalah cara kita melakukan pemrograman menggunakan class dan objek. Class ibarat blueprint dan objek adalah hasil cetakan dari blueprint tersebut."
    show bg college classroom with fade
    gerry "Ok, sampai di situ saja untuk pertemuan ini. Saya juga ada pengumuman mengenai proyek kalian."
    gerry "Untuk proyek, kalian bisa berkelompok. Proyeknya adalah membuat game menggunakan teori PBO."
    $ PS += 1
    $ DS += 1
    hide gerry with dissolve
    "Pak Gerry meninggalkan kelas."

    show christine smile with dissolve
    christine "Halo, kenalin aku Christine."
    MC "Oh, salam kenal."
    christine "Kamu sudah dapat kelompok?"
    MC "Oh, belum.."
    christine "Kamu mau nggak sekelompok sama aku?"
    MC "Boleh-boleh."
    show christine smile with dissolve:
        xalign 1.0
        xzoom -1.0
    show joshua smile with dissolve:
        xalign 0.0
    joshua "Halo,.. eh kamu! Udah lama nggak ketemu. Kamu sudah dapat kelompok belum?"
    MC "Aku satu kelompok dengan Christine."
    joshua "Aku join boleh gak?"
    MC "(Aku menatap Christine meminta pendapatnya)"
    christine "Boleh-boleh, aku nggak masalah."
    joshua "Oke, terima kasih guys."

    scene bg college hallway with dissolve
    "Setelah kelas, kamu dihadapkan pada tiga pilihan"

    menu:            
        "Pergi ke perpustakaan":
            scene bg library big with dissolve
            "Kamu memutuskan untuk pergi ke perpustakaan untuk belajar."
            MC "(Lebih baik aku belajar lebih awal untuk memastikan aku paham materi.)"
            
            menu:
                "Belajar bahasa pemrograman":
                    $ PS += 1
                "Belajar algoritma pemrograman":
                    $ DS += 1
            "Kamu meningkatkan kemampuan pemrogramanmu."
        
        "Diskusi dengan Pak Gerry":
            scene bg college teacherroom with dissolve
            show gerry smile
            MC "Permisi Pak, ada yang mau saya diskusikan mengenai proyek."
            gerry "Oh, silahkan."
            "Kamu dan Pak Gerry mendiskusikan proyek PBO."
            $ DS += 2
            "Diskusi dengan Pak Gerry telah memberikanmu insight"

        "Istirahat di rumah":
            scene bg home bedroom with dissolve
            "Kamu memutuskan untuk pulang dan beristirahat di rumah."
            MC "(Istirahat dulu agar aku punya lebih banyak energi nanti.)"
            "Kamu merasa lebih segar setelah beristirahat."

    scene bg college outdoor with fade
    "Kamu janjian dengan kelompokmu untuk kerja kelompok."
    show christine smile with dissolve
    christine "Halo, Joshua sudah datang belum?"
    "Joshua belum datang... Setelah beberapa waktu tetap tidak datang, kamu memutuskan untuk menelponnya"
    joshua "Maaf ya aku nggak bisa ikut kerja, masih ada urusan.."
    christine "Yasudahlah, kita kerja berdua aja."

    scene bg college classroom with fade
    "Tiba waktunya untuk presentasi proyek."
    "Kamu dan kelompokmu mempresentasikan proyek dengan baik."
    show gerry laugh with dissolve
    gerry "Wah keren banget! Saya nggak nyangka ada yang bisa bikin proyek sebagus ini di semester awal."
    "Kamu senang mendengar pujian dari Pak Gerry" 

    scene bg college teacherroom with fade
    "Kamu bertemu kembali dengan Pak Gerry untuk evaluasi semester."
    gerry "Bagaimana perkuliahanmu satu semester ini?"
    MC "Menurut saya baik kok Pak, aman."
    gerry "Hmm.. saya lihat nilaimu bagus. Teruskan ya."
    MC "Ok, Pak."
    
    "MC bersiap-siap untuk semester ketiga."
    
    # jump