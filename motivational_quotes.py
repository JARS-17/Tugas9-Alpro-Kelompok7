import random

quotes = [
    "Jangan pernah menyerah, karena kamu lebih kuat dari yang kamu kira.",
    "Setiap langkah kecil menuju tujuan adalah kemenangan.",
    "Kesuksesan dimulai dengan langkah pertama.",
    "Berani gagal, berani sukses.",
    "Hari ini adalah kesempatanmu untuk mulai yang baru.",
    "Kesulitan adalah bagian dari proses menuju kesuksesan.",
    "Jangan ragu untuk melangkah, bahkan jika jalanmu tidak jelas.",
    "Kegagalan adalah batu loncatan menuju kesuksesan.",
    "Usaha tidak akan pernah menghianati hasil.",
    "Setiap hari adalah kesempatan untuk menjadi lebih baik.",
    "Tidak ada yang tidak mungkin jika kamu berusaha.",
    "Kunci kesuksesan adalah fokus pada tujuan, bukan hambatan.",
    "Tantangan adalah kesempatan untuk menjadi lebih kuat.",
    "Kerja keras membuahkan hasil yang luar biasa.",
    "Hidup ini terlalu singkat untuk tidak berusaha.",
    "Sukses bukan tentang apa yang kamu capai, tapi bagaimana kamu mencapainya.",
    "Jangan takut untuk memulai dari awal.",
    "Kesuksesan adalah hasil dari keputusan yang tepat dan waktu yang tepat.",
    "Setiap hari adalah kesempatan untuk menciptakan sesuatu yang luar biasa.",
    "Hidupmu adalah hasil dari pilihanmu."
]

def get_random_quote():
    return random.choice(quotes)
