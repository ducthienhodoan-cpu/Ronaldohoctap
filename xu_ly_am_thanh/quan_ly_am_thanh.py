# Thu muc: xu_ly_am_thanh
# File: quan_ly_am_thanh.py
# Mo ta: Quan ly am thanh nhac nen Piano Sunrise, hieu ung va Giong noi AI

import os
import math
import struct
import wave

# Thu nhap pygame.mixer cho phat am thanh uu viet tren Windows
USE_PYGAME = False
try:
    import pygame
    pygame.mixer.init()
    USE_PYGAME = True
except Exception:
    USE_PYGAME = False

from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
from PyQt6.QtTextToSpeech import QTextToSpeech

DIR_AM_THANH = os.path.join(os.path.dirname(__file__), "..", "am_thanh_cache")

def tao_file_wav_dap_an(file_path):
    """Tao file am thanh hieu ung chuong ngan khi chon dap an."""
    if os.path.exists(file_path):
        return
    sample_rate = 22050
    duration = 0.15
    n_samples = int(sample_rate * duration)

    with wave.open(file_path, "w") as wave_file:
        wave_file.setnchannels(1)
        wave_file.setsampwidth(2)
        wave_file.setframerate(sample_rate)
        
        data = bytearray()
        for i in range(n_samples):
            t = i / sample_rate
            sample = int(16000 * math.sin(2 * math.pi * 587 * t) * (1 - i / n_samples))
            data.extend(struct.pack("<h", sample))
        wave_file.writeframes(data)

def tao_file_wav_ai_hoan_thanh(file_path):
    """Tao file am thanh hieu ung 3 note nhac khi AI hoan thanh suy nghi."""
    if os.path.exists(file_path):
        return
    sample_rate = 22050
    duration = 0.45
    n_samples = int(sample_rate * duration)

    freqs = [523.25, 659.25, 783.99]
    with wave.open(file_path, "w") as wave_file:
        wave_file.setnchannels(1)
        wave_file.setsampwidth(2)
        wave_file.setframerate(sample_rate)
        
        data = bytearray()
        for i in range(n_samples):
            t = i / sample_rate
            f_idx = min(2, int(t / 0.15))
            freq = freqs[f_idx]
            sample = int(18000 * math.sin(2 * math.pi * freq * t) * (1 - (i % (n_samples // 3)) / (n_samples // 3)))
            data.extend(struct.pack("<h", sample))
        wave_file.writeframes(data)

def tao_file_wav_ai_suy_nghi(file_path):
    """Tao file am thanh hieu ung bip bip khi AI dang suy nghi."""
    if os.path.exists(file_path):
        return
    sample_rate = 22050
    duration = 0.1
    n_samples = int(sample_rate * duration)

    with wave.open(file_path, "w") as wave_file:
        wave_file.setnchannels(1)
        wave_file.setsampwidth(2)
        wave_file.setframerate(sample_rate)
        
        data = bytearray()
        for i in range(n_samples):
            t = i / sample_rate
            sample = int(12000 * math.sin(2 * math.pi * 1046.50 * t) * (1 - i / n_samples))
            data.extend(struct.pack("<h", sample))
        wave_file.writeframes(data)

def tao_file_wav_nhac_nen(file_path):
    """Tao file am thanh nhac nen thu gian nhe nhang."""
    if os.path.exists(file_path):
        return
    sample_rate = 22050
    duration = 4.0
    n_samples = int(sample_rate * duration)

    notes = [261.63, 329.63, 392.00, 440.00, 523.25]
    with wave.open(file_path, "w") as wave_file:
        wave_file.setnchannels(1)
        wave_file.setsampwidth(2)
        wave_file.setframerate(sample_rate)
        
        data = bytearray()
        for i in range(n_samples):
            t = i / sample_rate
            note_idx = int(t * 2) % len(notes)
            freq = notes[note_idx]
            sample = int(8000 * math.sin(2 * math.pi * freq * t))
            data.extend(struct.pack("<h", sample))
        wave_file.writeframes(data)

class QuanLyAmThanh:
    """Class quan ly am thanh nhac nen, hieu ung va Giong noi AI."""
    
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = QuanLyAmThanh()
        return cls._instance

    def __init__(self):
        os.makedirs(DIR_AM_THANH, exist_ok=True)
        self.file_dap_an = os.path.abspath(os.path.join(DIR_AM_THANH, "dap_an.wav"))
        self.file_ai_done = os.path.abspath(os.path.join(DIR_AM_THANH, "ai_hoan_thanh.wav"))
        self.file_ai_thinking = os.path.abspath(os.path.join(DIR_AM_THANH, "ai_suy_nghi.wav"))
        
        file_gut_genug = os.path.abspath(os.path.join(DIR_AM_THANH, "gut_genug.mp3"))
        file_piano = os.path.abspath(os.path.join(DIR_AM_THANH, "Piano Sunrise (1).mp3"))
        if os.path.exists(file_gut_genug):
            self.file_nhac_nen = file_gut_genug
            self.ten_bai_nhac = "GUT GENUG - KITSCHKRIEG feat. BLUMENGARTEN & SHIRIN DAVID"
        elif os.path.exists(file_piano):
            self.file_nhac_nen = file_piano
            self.ten_bai_nhac = "Piano Sunrise"
        else:
            self.file_nhac_nen = os.path.abspath(os.path.join(DIR_AM_THANH, "nhac_nen.wav"))
            self.ten_bai_nhac = "GUT GENUG"
            tao_file_wav_nhac_nen(self.file_nhac_nen)

        tao_file_wav_dap_an(self.file_dap_an)
        tao_file_wav_ai_hoan_thanh(self.file_ai_done)
        tao_file_wav_ai_suy_nghi(self.file_ai_thinking)

        self.danh_dang_phat_nhac_nen = False
        self.am_luong_nhac_nen = 0.3
        self.use_pygame = USE_PYGAME


        if self.use_pygame:
            try:
                pygame.mixer.music.load(self.file_nhac_nen)
                pygame.mixer.music.set_volume(self.am_luong_nhac_nen)
                
                self.sound_dap_an = pygame.mixer.Sound(self.file_dap_an)
                self.sound_ai_done = pygame.mixer.Sound(self.file_ai_done)
                self.sound_ai_thinking = pygame.mixer.Sound(self.file_ai_thinking)
            except Exception as e:
                print("Loi khoi tao pygame mixer:", e)
                self.use_pygame = False

        if not self.use_pygame:
            try:
                self.player_bg = QMediaPlayer()
                self.audio_bg = QAudioOutput()
                self.player_bg.setAudioOutput(self.audio_bg)
                self.audio_bg.setVolume(self.am_luong_nhac_nen)
                self.player_bg.setLoops(QMediaPlayer.Loops.Infinite)
                self.player_bg.setSource(QUrl.fromLocalFile(self.file_nhac_nen))

                self.effect_dap_an = QSoundEffect()
                self.effect_dap_an.setSource(QUrl.fromLocalFile(self.file_dap_an))
                self.effect_dap_an.setVolume(0.7)

                self.effect_ai_done = QSoundEffect()
                self.effect_ai_done.setSource(QUrl.fromLocalFile(self.file_ai_done))
                self.effect_ai_done.setVolume(0.8)

                self.effect_ai_thinking = QSoundEffect()
                self.effect_ai_thinking.setSource(QUrl.fromLocalFile(self.file_ai_thinking))
                self.effect_ai_thinking.setVolume(0.5)
            except Exception as e:
                print("Loi khoi tao am thanh PyQt6:", e)

        try:
            self.tts = QTextToSpeech()
            self.tts.setVolume(1.0)
        except Exception:
            self.tts = None

        # Tu dong phat nhac nen khi khoi tao
        self.phat_nhac_nen()

    def bat_tat_nhac_nen(self):
        """Bat hoac tat nhac nen Piano Sunrise."""
        if self.danh_dang_phat_nhac_nen:
            self.dung_nhac_nen()
        else:
            self.phat_nhac_nen()
        return self.danh_dang_phat_nhac_nen

    def phat_nhac_nen(self):
        """Phat nhac nen Piano Sunrise trong vong lap vô hạn."""
        try:
            if self.use_pygame:
                pygame.mixer.music.play(-1)
            elif hasattr(self, 'player_bg'):
                self.player_bg.play()
            self.danh_dang_phat_nhac_nen = True
        except Exception as e:
            print("Loi khi phat nhac nen:", e)

    def dung_nhac_nen(self):
        """Dung phat nhac nen."""
        try:
            if self.use_pygame:
                pygame.mixer.music.stop()
            elif hasattr(self, 'player_bg'):
                self.player_bg.stop()
            self.danh_dang_phat_nhac_nen = False
        except Exception as e:
            print("Loi khi dung nhac nen:", e)

    def dat_am_luong_nhac_nen(self, phan_tram):
        """Thiet lap am luong nhac nen tu 0 den 100."""
        try:
            val = max(0, min(100, phan_tram)) / 100.0
            self.am_luong_nhac_nen = val
            if self.use_pygame:
                pygame.mixer.music.set_volume(val)
            elif hasattr(self, 'audio_bg'):
                self.audio_bg.setVolume(val)
        except Exception as e:
            print("Loi thiet lap am luong:", e)

    def lay_am_luong_nhac_nen(self):
        """Lay phan tram am luong nhac nen tu 0 den 100."""
        return int(self.am_luong_nhac_nen * 100)

    def lay_ten_bai_hat_nen(self):
        """Lay ten bai hat nhac nen dang dung."""
        return self.ten_bai_nhac

    def phat_hieu_ung_dap_an(self):
        """Phat am thanh khi dua ra hoac chon dap an."""
        try:
            if self.use_pygame and hasattr(self, 'sound_dap_an'):
                self.sound_dap_an.play()
            elif hasattr(self, 'effect_dap_an'):
                self.effect_dap_an.play()
        except Exception:
            pass

    def phat_hieu_ung_nut_bam(self):
        """Phat am thanh khi nhan nut bam."""
        self.phat_hieu_ung_dap_an()

    def phat_hieu_ung_tra_loi_dung(self):
        """Phat am thanh khi nhan nut hoac tra loi dung."""
        self.phat_hieu_ung_dap_an()

    def phat_hieu_ung_ai_hoan_thanh(self):
        """Phat am thanh khi AI hoan thanh suy nghi."""
        try:
            if self.use_pygame and hasattr(self, 'sound_ai_done'):
                self.sound_ai_done.play()
            elif hasattr(self, 'effect_ai_done'):
                self.effect_ai_done.play()
        except Exception:
            pass

    def phat_am_thanh_ai_suy_nghi(self):
        """Phat am thanh bip bip khi AI dang suy nghi."""
        try:
            if self.use_pygame and hasattr(self, 'sound_ai_thinking'):
                self.sound_ai_thinking.play()
            elif hasattr(self, 'effect_ai_thinking'):
                self.effect_ai_thinking.play()
        except Exception:
            pass

    def phat_giong_noi_ai(self, text):
        """Doc giong noi AI loi giai chi tiet cho hoc sinh."""
        try:
            if hasattr(self, 'tts') and self.tts:
                self.tts.stop()
                self.tts.say(text)
        except Exception as e:
            print("Loi khi phat giong noi AI:", e)

    def dung_giong_noi_ai(self):
        """Dung giong noi AI khi dang doc."""
        try:
            if hasattr(self, 'tts') and self.tts:
                self.tts.stop()
        except Exception:
            pass
