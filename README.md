# Whisper Tests

Collection of experiments on OpenAI Whisper models.

Tested on RTX 4090 24Gb.

## Samples

1. https://www.youtube.com/watch?v=UL7G4ugE8nU (ru)
2. https://www.youtube.com/watch?v=w1u65BctsU4 (ru)
3. https://www.youtube.com/watch?v=8qM-WESysZo (ru)
4. https://www.youtube.com/watch?v=fAtXX-gsxl0 (ru)
5. https://www.youtube.com/watch?v=F8UI4ek6ukc (ru)
6. https://www.youtube.com/watch?v=u4RkkjiYu0k (en)
7. https://www.youtube.com/watch?v=gggehz298L8 (en)
8. https://www.youtube.com/watch?v=jCuEBVbmPcA (en)
9. https://www.youtube.com/watch?v=wjO6OLmZB9A (en)
10. https://www.youtube.com/watch?v=Jy6Qk_bO3Qw (en)

## Tests results

Accuracy is calculated as [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance) ratio between
reference and transcribed texts.

### Reference tests (float32)

* Engine: openai_whisper
* Model: large-v2
* Type: float32

| №  | Audio Time (s) | Transcribe Time (s) | Accuracy (ratio) |
|----|----------------|---------------------|------------------|
| 1  | 823            | 80.51               | 1                |
| 2  | 856            | 99.76               | 1                |
| 3  | 416            | 45.68               | 1                |
| 4  | 1390           | 127.46              | 1                |
| 5  | 2205           | 233.90              | 1                |
| 6  | 922            | 88.75               | 1                |
| 7  | 1177           | 108.49              | 1                |
| 8  | 1505           | 146.07              | 1                |
| 9  | 1575           | 173.49              | 1                |
| 10 | 1714           | 202.24              | 1                |

* MAX VRAM used: 10.6Gb
* AVG Transcribe Time: 132.5s

### float16 (half)

* Engine: faster_whisper
* Model: large-v2
* Type: float16

| №  | Audio Time (s) | Transcribe Time (s) | Accuracy (ratio) |
|----|----------------|---------------------|------------------|
| 1  | 823            | 56.57               | 0.97             |
| 2  | 856            | 51.79               | 0.95             |
| 3  | 416            | 25.82               | 0.99             |
| 4  | 1390           | 77.26               | 0.94             |
| 5  | 2205           | 134.72              | 0.94             |
| 6  | 922            | 45.24               | 0.93             |
| 7  | 1177           | 64.26               | 0.99             |
| 8  | 1505           | 89.33               | 0.97             |
| 9  | 1575           | 99.32               | 0.96             |
| 10 | 1714           | 116.59              | 0.98             |

* MAX VRAM used: 8.41Gb
* AVG Accuracy: 0.96
* AVG Transcribe Time: 77.5s

### int8

* Engine: faster_whisper
* Model: large-v2
* Type: int8

| №  | Audio Time (s) | Transcribe Time (s) | Accuracy (ratio) |
|----|----------------|---------------------|------------------|
| 1  | 823            | 30.88               | 0.97             |
| 2  | 856            | 32.70               | 0.94             |
| 3  | 416            | 16.21               | 0.99             |
| 4  | 1390           | 48.94               | 0.93             |
| 5  | 2205           | 85.69               | 0.94             |
| 6  | 922            | 28.30               | 0.93             |
| 7  | 1177           | 39.74               | 0.98             |
| 8  | 1505           | 53.19               | 0.97             |
| 9  | 1575           | 62.52               | 0.96             |
| 10 | 1714           | 73.35               | 0.98             |

* MAX VRAM used: 4.6Gb
* AVG Accuracy: 0.96
* AVG Transcribe Time: 46.5s

### int4

* Engine: faster_whisper
* Model: large-v2
* Type: int4

| №  | Audio Time (s) | Transcribe Time (s) | Accuracy (ratio) |
|----|----------------|---------------------|------------------|
| 1  | 823            | 36.01               | 0.96             |
| 2  | 856            | 39.24               | 0.94             |
| 3  | 416            | 19.36               | 0.99             |
| 4  | 1390           | 57.84               | 0.94             |
| 5  | 2205           | 99.64               | 0.95             |
| 6  | 922            | 37.69               | 0.93             |
| 7  | 1177           | 52.48               | 0.98             |
| 8  | 1505           | 71.51               | 0.97             |
| 9  | 1575           | 80.40               | 0.96             |
| 10 | 1714           | 91.19               | 0.98             |

* MAX VRAM used: 3.9Gb
* AVG Accuracy: 0.96
* AVG Transcribe Time: 51.5s
