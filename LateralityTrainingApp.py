import time
import random
import string
import win32api
from configparser import ConfigParser 
import wx.lib.agw.hyperlink as hl
import webbrowser
import os
import wx
import wx.lib.agw.pygauge as PG
import wx.lib.agw.gradientbutton as GB
from wx.adv import SplashScreen as SplashScreen
from wx.lib.embeddedimage import PyEmbeddedImage

import xlwt

Error = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAAAXNSR0IArs4c6QAAAARnQU1B'
    b'AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAJTSURBVGhD7ZgxcoMwEEXtXMEpyUG4'
    b'g1sOQptDpM0d3KZO6zukJpPKOQP531oRI0DRSsKGid+MBoEQfHYR+mhzx0PbtoVU1wke4E2q'
    b'6wPiKxRSyqF1AeFHo7/9kkPrAaJt9C2VNK0DCD4Z3R0naVo+EOtG3zJLFrayzQaVStXle7vd'
    b'Pko9Gw+yzQK011IdYzdXFrLB6F/SNI3UeixzcoOwF6MP38/jsS2Kgq/SuTgczh2WBEQVRpuh'
    b'qqpOPMvhcJCWjmVlAYI6hXxteOiyMBsO2SxG8iCGGFoF7eDco1+WLOT4Cj3LVsurbJNIegBE'
    b'kZHfmz01zMJtjR4EWMPWg01umeB2Rg83n7IMmgcgSZNbtJXAjWnQdmavDyyD1H7B+VIbkGQx'
    b'osaARG1UfARJFiMqA7jhZDiJMgMkOgvqDECIz7DFEp0FdQb+ij6JyIDlCX0/pR6EKgMQ8SLV'
    b'uVBfPzgDEM+pvzF7fhIyQFRZ0GRg7uhbsliMHoheiRIMu7hFSbDRC81ArGGLJV8WEI1JyzAF'
    b'u7klgjxGDxcaNWw+Ln8nbZn4P/aRbvRwEXX0Cf+J2d2Wuq6lRU2S0eMDuCtswVA0L5EgnsSv'
    b'6KFzVPRnwJuFyYmMPaV6a7xGb/QzCu1zGLZYaPR0ehj9VMqyPI8BrhFFfIHGCJvccOJgFUqL'
    b'u7DF/QyMriX1xgBOCjZsPhLNnI+B0XPHwLUMWyzTFgMRUhk2HzO9QpbxsYCGd9OeDgetfQgO'
    b'5swMxwIOLmXSCqWb3M6jDQc+sMm1THIVfJPbnTv/h83mB+Qgj84hoWTNAAAAAElFTkSuQmCC')

SplashScreenImg = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAAfQAAAE7CAIAAACkCuS8AAAAAXNSR0IArs4c6QAAAARnQU1B'
    b'AACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAABabSURBVHhe7d1tYuMos4bhs4jZlhfk'
    b'zWQt3opX0kcfIEFRQCHZfq3yff2a2FAUSHqS6XTS//cfAMAdwh0AHCLcAcAhwh0AHCLcAcAh'
    b'wh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAh'
    b'wh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAh'
    b'wh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAh'
    b'wh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAh'
    b'wh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhwh0AHCLcAcAhF+F++3v+Szz/'
    b'buGNQaLOv3+Pe3in6v4IQ/vSYgenKS3unpPH4+9+G9/9gY2vBk9ebHtfZfw85IxWx3Ks6QY5'
    b'eIm+6wJVDzzI3++fi+hD1vvwcg23+9/fYz7wMHW1XoDpCoRRzhHuO+W57JY6GAEHp6k9Kp6P'
    b'ofv3yMZXgydfffgPnIdsurp2sTtbRhy8RN91gaoHHshN9qqKRmS9Dy+nud2nTA/jm57zp9kw'
    b'ySnCfaM+lr1aByPg4LRKkyrLk7A6tPHV4MlXH/5D5yEn6Tu2jSodvETfdYGqBx6Um2yXFZ3I'
    b'eh9eTphzPYy0mhLecptfFOEeVR7mTrHKLE16ax6cVnnOK4zncGzjq8GTF0vtWzt2HsVhlE+/'
    b'HGK/Nw5eou+6QNUDD7TSrbpid7Leh5dLjZy7MPZ/URdCuAeVJ6hXrTqtlN6aB6eN3sOtpyE6'
    b'uPHV4MmLtfb2jp6HnCcbkO9bDiQ42NJ3XSAxt1hOr13vSuxODvzwcpuxQ1dY7vXrIdxX1Sdo'
    b'Ur/5pN7NvckHDjTc2OpN+d/SfuvnNj548sbzMR+j8ling+WbJx5hc0vfdYF6bdeK1wqL3clh'
    b'H14uqFRd/lA9++b1dAHuf9of3Zy4Mb4Z4b6o3XWr2r1X6N3cm3zgQMO9rYoOupVPbnzw5I3n'
    b'Yz7GmdzB3oN8x3wZFeaWvusC9dquV9crd9L2w8vNxJBF99vV2WdZt38qQ7jP5A3yfIhP7/qt'
    b'V+rd3Jt84EDD3a2aW5id3vjgyRubG9pDsYkwvtjb6F2RMbf0XReot5h4P6OVFv3IIR9eblJW'
    b'tF7nNeD9JvuEcFeeoGl+7zbVmWflAwca7m51pPHzGx88eWPxsR6K8do++kXazC191wXqDZan'
    b'lCtri4bkgA8vV5xP9wb8LYR7cYest5C4D201ezf3Jh840HBvqyNtv2DjgydvPB/zMW7EjH/y'
    b'rzoPnLDO3NJ3XaBe2/n78md+ygmiI/n2h5eT53P6KjtDuOtP0NgzFPVu7o0Y2JIXaWz1druL'
    b'rbQ6eM3GB0/eeD7mY9zJzeQsFdrMLX3XBeq1nb8/VRIT5BTRkqz3v12ud/f9nJ8Pd3l77TfQ'
    b'gVtHTClu7k1xU9c1b/eOegMv2vjgyRvPx3yMqfqRvuKhN7f0XReo13b+/lJILptNGkvbNy83'
    b'ePP9nl8Pd3FvZVPHy/Zu7k1xS9flRURPTc2GX7PxwSMyno/5GDO1ozFObzO39F0XqNd2/n6o'
    b'Iyal08TCst5nl+ut9vN+PNzF/SFmyge1e/uYb7fihq7Li8iWqp7tZl+08cGTN56P+RgF7VQH'
    b'boYWc0vfdYF6befvb4sUBxkninVlvc8u11ttVyxQ0ShxRT8d7vIRKSZan6HIfLtZ77ZJXkR2'
    b'pOr+xoyXbVyM65288XzsT61Qno59bpu5pe+6QL228/eTVcTEOFUsK+t9drnearuifEWjxBX9'
    b'crgbHhDjMxSZb7fqXd4jGypYfhPS6zYuhvU2Yjwf+1MrDfZjZ27puy5Qr+3GfSimrpPFqrLe'
    b'Z5cT7zYudlG8omj42n443OXjYdK+/L2be9O4y9vKrcpt9Iu9cOODJ288H/MxFgb7sTO39F0X'
    b'qNd28z4Uk+fpojNZ73+7XP1gi9K6/pW5lt8N90NPUKd47+beNO/yFm2r8tatL7t45cYHT954'
    b'PuZjLBy6EyzMLX3XBeq1nb9fVJCNy7+aLut9eLliQu1gi8K62vSr+tlwN17vUqu6KFq/WfKB'
    b'poZX6lZlGjTrvXTjgydvPB/zMRaO3Akm5pa+6wL12s7f7xcQZL0PL6eMr1+Ykpw8MvcSfjXc'
    b'23dRU6O8qFq/W/KBloaDylbt6fHajQ+evPF8zMdYOHAn2Jhb+q4L1Gs7f19rSjaekfU+vNyk'
    b'HG/9R67kOdevyGX9aLjLKzukXr93c2/6d3lFdatyR5W1X7zxwZM3no/5GAvjd4KRuaXvukC9'
    b'tvP39eMSO0rJeh9ebqEdWC/gy5+MrV2OS/vJcJf3z/CE2p3Qu7k3lrtcVd+qZVMv33i9HZXx'
    b'fMzHWBjsx87cUr0Dy+FbxmTkBNFYr23bfSgX2ch6H14uEKtGT/UXus//bHYYkKhUvjiP4a7b'
    b'b6XhJ6icYrvN6rdM5X7U5EVEI1nrsmix/Os3Lt9W7csYz8d8jIXW8Zxibum7LlCv7fz9+nKV'
    b'6yzrfXi5TWW8VbXuxf1guLcfhwrbpN7NvREDW/Iioo/8+SjOoTn3FRsvVtTsTRrPx3yMhebx'
    b'nGFuqdlBcVzt0zRtvDmp13b+fuu4itZnst6Hl0upEywc/0b33wv35sNQZ5pmjgAxsCUvItqQ'
    b'z4esm77/jo3LN1V7E8bzMR9joXM8x5lb+q4L1Gs7f799XMq1lvU+vJyQ/ftKJtZvvl7Uz4W7'
    b'fLo6N8xOLqLdmr2beyO7aMiLiC7KJqr7e8vGR05+Yjwf8zEWusdzlLml77pAvbbz93vHVVxt'
    b'We/Dy2mWP1UP41uc5/ri18Jd3H69+yvTn9u7uTdiYEtepJsdtUfiPRsfOPmZ8XzMx1joH89B'
    b'5pa+6wL12s7f768pepf1Prxcw/Kt04f850Cmjx/Ld1nDKOdchDsAIEe4A4BDhDsAOES4A4BD'
    b'hDsAOES4A4BDhDsAOES4A4BDhDsAOES4A4BDhDsAOES4A4BDhDsAOES4A4BDhDsAOES4A4BD'
    b'hDsAOES4A4BDhDsAOES4A4BDhDsAOES4A4BDhDsAOES4A4BDhDsAOES4A4BDhDsAOES4A4BD'
    b'hDsAOES4X9398a/iOXs8/u63WxiruP09w/CCZXrN7Xb/ezymAqHWYq73N9ULY46biv/NxfPW'
    b'13at9d+z8aLq4x7esRmff3ZFuEW4X1093FPPRyXzGhmXqE4vzKHerziF/KGMv92nTA81mvoL'
    b'vHrjC6Xo82+kQHk1O1ldrji2IPwi3K/OFu4z9am3Zdys/xXhzZLruymAB2JozvUw0aq5wCs3'
    b'Hqk1R8J2+JODtiJfumNBuF+dPdzVoLBnXDtnRuqkbF8ZH60+Ofe/LCtjPlcuxUC6axWGT31g'
    b'PXhGuF/dSLgrX9WNxWbli8IT2Tvp5fu56hM17V6y8Uz1SpjTVu+pMV1fki/dMSPcr04838mD'
    b'fbspf5QhH3yRJ2mQWKbP9ISZv3mafUtybqf25zaNOKpE5lo9Tb2pvF5fD8cXbDxXzfZJf/ai'
    b'ttdauo+Ox08h3K9OPOBFjIj35YPfyLhFZ7oaMO3vQk4RrySwHn/al7Ld73Fm0VwdfHrjgnIO'
    b'CVO6a7tdVBavLmn8XALfCPerE094+Vy3B/Qybmz6pJuCC9u8Mr1s1af6S8C3Pg2c3Lgg9/N8'
    b'iK/9LXlbbjdSZ9eHW08JrhHuV9fNoPaAcxkn82UkVYpskq0XnwBemlkvDfci26dqI/MXxX4T'
    b'yuzi/BL9xeAf4X51vQwR78sQ62Vcc7rMl8FMaU/XAvOFTm1ckK2uGxmpMJPHkeld19yLzwqX'
    b'RLhfnXjI0xCYv4MpvxiUIdHIuO700fQq6KEYnK7edmbjQm0bYzuQDYmf1hINyMv+qN8G+FGE'
    b'+9WJp7yjeOhlMLVl0xvxaNVK2PPVm05sXJBXYB87lO4yru/FC2HgrDgd8emo1S9+BOF+dSPh'
    b'rqTLSMaJ6WLqoTzJu08XaEXbK5zYeE40mo0tMrheRxlaP5yhwfhRhPvViWype6r5aM64cvor'
    b'4rceSfbq1hPIS5zYeEasLlJVrlKvpe23djpKtsvX2k3jFxDuV2eKtvpvWTFlnD79FXFSiy89'
    b'7HSmE5jkJU5sPCGriGwvB9T2IcaFOvrxjIzF7yLcr64ebfNvrpU/JlroZlw93vSMGdIoYa/+'
    b'pnDv5fpMFlGi2zBkJjYRRqmHUDkZ8XLtswh+BuF+dXoqmJVJIdOoHqti6Ub+VsilsubN1Y3h'
    b'Lgqc2XgkZ5ioV6jspvp6bag4h373cI5wv7qXh3uZltWa5oG6znRrdTmuQkw/tfGVKGGlxa5Y'
    b'eV+4bLOW7fUa+E2E+9WdfKTVrJCppcXRQqZhdaBCzi1b749okJPl3HMbnxXtWZVV64ldvFX/'
    b'6++NIvhFhPvViYh5SbjbU06Os2ZKOU/rXKne+61hgQzesquTGz+R7UrR1kVUjmqXjTx5K8AZ'
    b'wv3q3hPuZXbVCisZ1/k7Jsov1K2WV6p3A36qH0ZulOpnN651ZibSvdrLorFS3lu7DH4N4X51'
    b'4tGvZXBNPRDEO/WsqITP+hd1kjnzT/VX/gnURte16kX5en21+rmNmw8nkhOynjrXsJrunYGN'
    b'U8UPINyv7uQDXc+4MlSqtWVyjekF47nqta5PbVy21M32ckpSs9XKopLuvbYMXcExwv3q3hju'
    b'RSA1qhdDjWwBdLT61HCt/JmNy7dNh16f1L+Earr3x5n6gleE+9W9M9zLVGllsfK7FNus3x1d'
    b'qH9S39Quf2Ljh7K9Pq3TyUJJd21VSyn8CsL96t4b7mWsdBaYMzjPMM1zKNd3y5+qhxothvLH'
    b'Nz54IjuZ7mFN0xWUi1aC21QLv4Fwv7qTj3P/az0ZSaYlphSev7kpwmzK9N6vQzBZvnV6svzh'
    b'jYsD10O2Qpvbb2Qmm7ENG2oOzhDuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4A'
    b'DhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4A'
    b'DhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4A'
    b'DhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4A'
    b'DhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4A'
    b'DhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4A'
    b'DhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4A'
    b'DhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4A'
    b'DhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4A'
    b'DhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4A'
    b'DhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAF7r/vi3eNzDCx9y+3su6z7/buGVb9A5'
    b'jfcdFuEO4LUI9xThDsAJwj1FuANwgnBPEe4Arul2fzzXVJ1y9fm4Tx+vH+R5lQ6bx/3dtwjW'
    b'Uzm+mtZpFKmWuf899in5jCRb/+ZhcdyyjTAi0Vw9MJ7GZn+7mBlGVD8BdCoT7gCOmwJpTRhF'
    b'Ejr6sD2FQ06lsVxGda+IEu7qlCk4w9vbwpp02KS3+sx4GilTA3FnaQ39U1mCcAdw1JZMz/hF'
    b'7PzlZ3htj6JtWPxydPpqOoyKY+KQYs5AkSLu4pTYXbnsXnWOUll3H2ZYPRnTPo2crYEyybW8'
    b'zxHuAA6KwZQHTIyd+LL+JaYMp/zjYo6liBijTpEvxi3kdeXOLKsbT0OyNVDtu1J1RrgDOEaE'
    b'26YSerot1NL4KhPPUkQEYJiy11jozYlBMjxHVu+chmRrYH9hGSh2qiPcARxjjLN2Miaztzx7'
    b'yGCzFRGRl6bhTm+uk60jqydNL2qvB7YGZvsr5Xsawh3AQXrIxDSLL3fSLbHNXGR5ZykSx4SJ'
    b'4sOVfDFuQYSr2JlldeNpSLYGFluplZhRINwBHBUjaAqaxrcQt1DaRs3fM3zM30AU8ZTGl8gu'
    b'Q5E4ZJu5B+c6pfVN0PY3VE1bsJ2GYGxgkR7Pvssawh3AcVneCEkyVf6OYBlQW9YpWdgrUoR7'
    b'ZcqUouHtNFsLojnLFoynkbI3MNtHV8olCHcApyxfwobImYLzb/pw/e88f9Kf0ZnG6T8CFONL'
    b'ybVFs4gS7pNsSv2HmJafIVr/Wxm2smzBeBqbrYF5ZK+BbXjtfFKEO4DftYd7eOGr6Z++Kgh3'
    b'AL/rUuE+1izhDuB3XSncB/5IZka4A/hd1wn3oT+SmRHuAOAQ4Q4ADhHuAOAQ4Q4ADhHuAOAQ'
    b'4Q4ADhHuAC4u/i3B7e8zrr9JIP0dMj+IcAdwcSLc44fX+NGktyHcAVwcX7lrCHcAF1eEOyaE'
    b'O3BV4Ufn00hbXkp+QH2PvfcNDi8Uit+1K375rVIhrBuXCR+GX4cbaz23f9ViFsdE89xYWdR5'
    b'/t2TX6sby6RtTl3ulVfFr/CVAxSGXw3cLnum4Q3hDlyWyMIi1LL8fN9gzfoHI7rhcFdsf+Qi'
    b'x8xzZbf1Os8khINtixN1F+0/7YlrS+msbtnDDacId+C68jDcc0W8sMbG+wYXtnBq/YNzSo18'
    b'1b3MnHyxztbKPk9Wih+XdUKZfT976e21OGubFjexr13ZtrbxdefzIuFjS9mDDecId+DCQgos'
    b'j3caAEtOhBdkWL1hsBCzKc/ArUp4OX6cjEoX3T+U6xTlZaX4saxTrqS+tr4kiyzUFzftd1em'
    b'socalgh34MpCLEypEJ70+P/t05d321th7BsHZ8LbReaI15VhcaU844p1wuvbTFkpftyoI4fM'
    b'8rL64krTu1q/KVPZQw1LhDtwaeGhT5I3JsP6SpYi7xucEkm1Ea8rw0SoiQ834fVtpqwUP27U'
    b'0XrMy+qLa/M2tX5TprKHGpYId+Da4lO/WB7z+MzPKiGyeOnglB46W7n4chi2F5IBFuuIpYry'
    b'cl78OM4rFiqnzPK6sshCfXHTfndlKnuoYYlwBy4uPvaT8JTHh16JmfcMXr9bur+0DWt9Q3Uv'
    b'P/1PQTpkq5Ostg6ZB2097ZEmgy9+HAuFOmnLcsosLhdfix83v/M5v6JsPPY7z3rkfxnSVHb5'
    b'eLThHOEOXJ3MsjQ/9nQI3jFYeTHO1OxZFCdmOm+vsvVl8Mm2Q510jpwyi8ulDSi7mD7RhLe3'
    b'GUlldcokmdUtG+uON5wi3IHLWx/8MgrSVzbvGCy/gF1MX5HuITZ/7Sp+iGl1SwbNo9ISe3il'
    b'X/gXP/ITetoLx49jQ2eycvnCe31dWbq+8W3Ov8oPMbXLrq8faXhDuAP4Uu3wQhvhDuBLEe5n'
    b'EO4AvhThfgbhDuBLEe5nEO4A4BDhDgAOEe4A4BDhDgAOEe4A4M5///0/dUiNNJsn6J8AAAAA'
    b'SUVORK5CYII=')


def GradientButton(parent, id = wx.ID_ANY, bitmap=None, label="", pos=wx.DefaultPosition, size=wx.DefaultSize, 
                           style=wx.NO_BORDER, align=wx.CENTER, validator=wx.DefaultValidator, name="gradientbutton"):
    Btn = GB.GradientButton(parent, id, bitmap, label, pos, size, style, align, validator, name)
    Btn.SetTopStartColour(wx.Colour(0, 0, 0))
    Btn.SetTopEndColour(wx.Colour(0, 0, 0))
    Btn.SetPressedBottomColour(wx.Colour(0, 0, 0))
    Btn.SetPressedTopColour(wx.Colour(0, 0, 0))
    Btn.SetForegroundColour(wx.Colour(20, 20, 20))
    return Btn
  


#main frame
class Frame(wx.Frame):
    def __init__ (self, Parent, *args, **kwargs):
        wx.Frame.__init__(self, Parent, style = (wx.DEFAULT_FRAME_STYLE))
        
        
        self.ConfigDir = wx.StandardPaths.Get().GetDocumentsDir()
        
        if os.path.isfile(self.ConfigDir + r"\config.ini"):
            cfg = ConfigParser()                                                                                                                                                                                                    
            cfg.read(self.ConfigDir + r"\config.ini")
            self.selection_method = cfg.get('data','Selection Method')
            self.program_language = cfg.get('data','Program Language')
        else:
            cfg = ConfigParser()
            cfg['data'] = {'Selection Method':'click', 'Program Language':'english'}
            with open(self.ConfigDir + r"\config.ini", 'w') as configfile:
                cfg.write(configfile)
            self.selection_method = 'click'
            self.program_language = 'english'
            
        #menubar
        menubar = wx.MenuBar()
        FileMenu = wx.Menu()
        self.ResponseMenu = wx.Menu()
        self.LanguageMenu = wx.Menu()
        HelpMenu = wx.Menu()
    
        self.hindi = self.LanguageMenu.Append(wx.ID_ANY, 'हिंदी', kind=wx.ITEM_CHECK)
        self.english = self.LanguageMenu.Append(wx.ID_ANY, 'ENGLISH', kind=wx.ITEM_CHECK)
        self.click = self.ResponseMenu.Append(wx.ID_ANY, 'Click', kind=wx.ITEM_CHECK)
        self.hover = self.ResponseMenu.Append(wx.ID_ANY, 'Hover', kind=wx.ITEM_CHECK)
        self.help = HelpMenu.Append(wx.ID_ANY, 'About')
        self.click_id = self.click.GetId()
        self.hover_id = self.hover.GetId()
        self.hindi_id = self.hindi.GetId()
        self.english_id = self.english.GetId()
        
        if self.selection_method == 'click':
            self.ResponseMenu.Check(self.click_id, True)
            self.ResponseMenu.Check(self.hover_id, False)
        else:
            self.ResponseMenu.Check(self.click_id, False)
            self.ResponseMenu.Check(self.hover_id, True)            
        
        if self.program_language == 'english':
            self.LanguageMenu.Check(self.english_id, True)
            self.LanguageMenu.Check(self.hindi_id, False)
        else:
            self.LanguageMenu.Check(self.english_id, False)
            self.LanguageMenu.Check(self.hindi_id, True)        
        
        self.Bind(wx.EVT_MENU, self.onclickresp, self.click)
        self.Bind(wx.EVT_MENU, self.onhoverresp, self.hover)
        self.Bind(wx.EVT_MENU, self.ifhindi, self.hindi)
        self.Bind(wx.EVT_MENU, self.ifenglish, self.english)
        self.Bind(wx.EVT_MENU, self.onhelp, self.help)
    
        FileMenu.Append(wx.ID_ANY, 'Selection Method', self.ResponseMenu)
        FileMenu.Append(wx.ID_ANY, 'Language', self.LanguageMenu)
        menubar.Append(FileMenu, '&File')
        menubar.Append(HelpMenu, 'Help')
        self.SetMenuBar(menubar)        
        
        #instances of panel classes
        self.initialpanel = InitialPanel(self)
        self.setpanel = SetPanel(self)
        self.photopanel = PhotoPanel(self)
        self.endpanel = EndPanel(self)
        self.nextpanel = nextpanel(self)
        
        #declaration of sizers
        self.mainsizer=wx.BoxSizer(wx.VERTICAL)
        
        #adding panel to sizers, and adding sizers to the mainsizer
        self.mainsizer.Add(self.initialpanel, 1, wx.EXPAND)
        self.mainsizer.Add(self.setpanel, 1, wx.EXPAND)
        self.mainsizer.Add(self.photopanel, 1, wx.EXPAND)
        self.mainsizer.Add(self.endpanel, 1, wx.EXPAND)
        self.mainsizer.Add(self.nextpanel, 1, wx.EXPAND)
        
        self.SetSizer(self.mainsizer)
        
        #showing only initialpanel
        self.mainsizer.Hide(1)
        self.mainsizer.Hide(2)
        self.mainsizer.Hide(3)
        self.mainsizer.Hide(4)
        
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        
    def OnClose(self, event):
        if self.click.IsChecked() and self.english.IsChecked():
            cfg = ConfigParser()
            cfg['data'] = {'Selection Method':'click', 'Program Language':'english'}
            with open(self.ConfigDir + r"\config.ini", 'w') as configfile:
                cfg.write(configfile)
        elif self.click.IsChecked() and self.hindi.IsChecked():
            cfg = ConfigParser()
            cfg['data'] = {'Selection Method':'click', 'Program Language':'hindi'}
            with open(self.ConfigDir + r"\config.ini", 'w') as configfile:
                cfg.write(configfile)
        elif self.hover.IsChecked() and self.english.IsChecked():
            cfg = ConfigParser()
            cfg['data'] = {'Selection Method':'hover', 'Program Language':'english'}
            with open(self.ConfigDir + r"\config.ini", 'w') as configfile:
                cfg.write(configfile)
        else:
            cfg = ConfigParser()
            cfg['data'] = {'Selection Method':'hover', 'Program Language':'hindi'}
            with open(self.ConfigDir + r"\config.ini", 'w') as configfile:
                cfg.write(configfile)
        
        self.Destroy()
        
    def onclickresp(self, e):
        self.ResponseMenu.Check(self.click_id, True)
        self.ResponseMenu.Check(self.hover_id, False)
        self.photopanel.leftBtn.Unbind(wx.EVT_MOTION, None)
        self.photopanel.rightBtn.Unbind(wx.EVT_MOTION, None)
        self.nextpanel.nextbtn.Unbind(wx.EVT_MOTION, None)
        self.nextpanel.nextbtn.Bind(wx.EVT_BUTTON, self.nextpanel.onnext)         
        self.photopanel.leftBtn.Bind(wx.EVT_BUTTON, self.photopanel.onleft)
        self.photopanel.rightBtn.Bind(wx.EVT_BUTTON, self.photopanel.onright)
        if self.english.IsChecked():
            self.initialpanel.Instructions.SetLabel(self.onclickeng())
        else:
            self.initialpanel.Instructions.SetLabel(self.onclickhin())
        self.initialpanel.Layout()  
        self.photopanel.Layout()
        self.setpanel.Layout()
        self.nextpanel.Layout()        
    
    def onhoverresp(self, e):
        self.ResponseMenu.Check(self.click_id, False)
        self.ResponseMenu.Check(self.hover_id, True)
        self.photopanel.leftBtn.Unbind(wx.EVT_MOTION, None)
        self.photopanel.rightBtn.Unbind(wx.EVT_MOTION, None) 
        self.nextpanel.nextbtn.Unbind(wx.EVT_BUTTON, None)
        self.nextpanel.nextbtn.Bind(wx.EVT_MOTION, self.nextpanel.onnext)        
        self.photopanel.leftBtn.Bind(wx.EVT_MOTION, self.photopanel.onleft)
        self.photopanel.rightBtn.Bind(wx.EVT_MOTION, self.photopanel.onright)        
        if self.english.IsChecked():
            self.initialpanel.Instructions.SetLabel(self.onhovereng())
        else:                      
            self.initialpanel.Instructions.SetLabel(self.onhoverhin())
        self.initialpanel.Layout()  
        self.photopanel.Layout()
        self.setpanel.Layout()
        self.nextpanel.Layout()                  
    def ifhindi(self, e):
        self.LanguageMenu.Check(self.english_id, False)
        self.LanguageMenu.Check(self.hindi_id, True)
        self.setpanel.timemsg.SetLabel("परीक्षा शुरू होने में {} सेकंड बाकि".format(self.setpanel.timeToLive))
        self.setpanel.set_num-=1
        self.setpanel.lbl.SetLabel("सेट {}".format(str(self.setpanel.set_num)))
        self.setpanel.set_num+=1
        self.photopanel.rightBtn.SetLabel('दाएं')
        self.photopanel.leftBtn.SetLabel('बाएं')
        self.initialpanel.InstructionTitle.SetLabel("निर्देश-")
        self.initialpanel.startBtn.SetLabel('प्रारंभ')
        self.initialpanel.Heading.SetLabel('पार्श्वता प्रशिक्षण मॉड्यूल')
        self.nextpanel.nextbtn.SetLabel('अगला')
        if self.click.IsChecked():
            self.initialpanel.Instructions.SetLabel(self.onclickhin())
        else:
            self.initialpanel.Instructions.SetLabel(self.onhoverhin())         
        self.initialpanel.Layout()  
        self.photopanel.Layout()
        self.setpanel.Layout()
        self.nextpanel.Layout()
                   
    def ifenglish(self, e):
        self.LanguageMenu.Check(self.english_id, True)
        self.LanguageMenu.Check(self.hindi_id, False)
        self.setpanel.timemsg.SetLabel("Starting test in {}s...".format(self.setpanel.timeToLive))
        self.setpanel.set_num-=1
        self.setpanel.lbl.SetLabel("SET {}".format(str(self.setpanel.set_num)))
        self.setpanel.set_num+=1
        self.photopanel.rightBtn.SetLabel('RIGHT')
        self.photopanel.leftBtn.SetLabel('LEFT') 
        self.initialpanel.InstructionTitle.SetLabel("Instructions:")
        self.initialpanel.startBtn.SetLabel('Start')
        self.initialpanel.Heading.SetLabel('Laterality Training Module')
        self.nextpanel.nextbtn.SetLabel('Next')
        if self.click.IsChecked():
            self.initialpanel.Instructions.SetLabel(self.onclickeng())
        else:           
            self.initialpanel.Instructions.SetLabel(self.onhovereng())            
        self.initialpanel.Layout()
        self.photopanel.Layout()
        self.setpanel.Layout()
        self.nextpanel.Layout()
            
    def onhelp(self, e):
        
        app = wx.App()
        frame = wx.Frame(None, title='About', size = (580,320))
        frame.Center()
        mainsizer = wx.BoxSizer(wx.VERTICAL)
        frame.SetBackgroundColour(wx.Colour(20, 20, 20))
        txt = wx.StaticText(frame) 
        heading = wx.StaticText(frame)
        heading.SetFont(font = wx.Font(15, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        heading.SetForegroundColour(wx.WHITE)        
        txt.SetFont(font = wx.Font(15, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        txt.SetForegroundColour(wx.WHITE)
        txt.SetLabel("The software 'Laterality Training Module' has been developed by Auptimo Technologies LLP, New Delhi. Other products by auptimo include GaitON, a motion analysis system with inbuilt protocols for posture, gait, and sports specific motion analysis. For more information visit our website or write to us at info@auptimo.com")
        heading.SetLabel('LATERALITY TRAINING MODULE')
        btn = GradientButton(frame, wx.NewId(), size = (120, 40))
        btn.SetFont(font = wx.Font(12, wx.ROMAN, wx.NORMAL, wx.BOLD))
        btn.SetLabel('Visit our website')
        btn.SetForegroundColour(wx.WHITE)
        btn.Bind(wx.EVT_BUTTON, self.visitwebsite)
        mainsizer.AddSpacer(15)
        mainsizer.Add(heading, 0, wx.ALIGN_CENTER)
        mainsizer.AddSpacer(13)
        mainsizer.Add(txt, 1, wx.EXPAND | wx.ALL, 15 )
        mainsizer.Add(btn, 0, wx.ALIGN_CENTER)
        mainsizer.AddSpacer(25)
        frame.SetSizer(mainsizer)
        frame.Show()
        frame.Layout()
        app.MainLoop()
    
    def visitwebsite(self, e):
        webbrowser.open('http://auptimo.com/')
    def onclickeng(self):
        txt = "Welcome to the laterality training module.\n \n 1. You would be shown different pictures of right and left hands / feet.\n\n 2. You are required to move the mouse to the right and click the right button\n     if you feel it's the right hand / foot and to the left and click the left\n     button if it's left hand / foot.\n \n 3. Each picture would appear for 5 seconds, and you would be required to reply\n     in the 5 seconds duration."
        return txt
    def onclickhin(self):
        txt = "पार्श्वता प्रशिक्षण मॉड्यूल में आपका स्वागत है। \n \n 1. आपको दाएं और बाएं हाथ / पैरों की अलग-अलग तस्वीरें दिखाई देगी। \n \n 2. आप कर्सर को दाईं ओर इंगित/ इशारा करें और दाएं बटन पर क्लिक करें यदि आपको लगता है कि \n     यह सही हाथ / पैर है और बाईं ओर इंगित/ इशारा करें और बाएं बटन पर क्लिक करें यदि आपको\n     लगता है कि यह सही हाथ / पैर है। \n \n 3. प्रत्येक तस्वीर 5 सेकंड के लिए दिखाई देगी और आपको 5 सेकंड की अवधि में जवाब देने की\n     आवश्यकता होगी।"
        return txt
    def onhovereng(self):
        txt = "Welcome to the laterality training module.\n \n 1. You would be shown different pictures of right and left hands / feet. \n\n 2. You are required to move the mouse to the right button if you feel it's the right\n     hand / foot and to the left button if it's left hand / foot.\n\n 3. Each picture would appear for 5 seconds, and you would be required to reply\n     in the 5 seconds duration."
        return txt
    def onhoverhin(self):
        txt = "पार्श्वता प्रशिक्षण मॉड्यूल में आपका स्वागत है। \n \n 1. आपको दाएं और बाएं हाथ / पैरों की अलग-अलग तस्वीरें दिखाई देगी। \n \n 2. आप कर्सर को दाईं ओर इंगित/ इशारा करें यदि आपको लगता है कि यह सही हाथ / पैर है और बाईं ओर\n     इंगित/ इशारा करें यदि आपको लगता है कि यह सही हाथ / पैर है। \n \n 3. प्रत्येक तस्वीर 5 सेकंड के लिए दिखाई देगी, और आपको 5 सेकंड की अवधि में जवाब देना होगा।"
        return txt
    

  
#panel for the startup page                    
class InitialPanel(wx.Panel):
    def __init__ (self, parent, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.SetBackgroundColour(wx.Colour(20, 20, 20))
        self.Heading = wx.StaticText(self) 
        self.Heading.SetFont(font = wx.Font(40, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        self.Heading.SetForegroundColour(wx.WHITE)
        
        self.startBtn = GradientButton(self, wx.NewId(), size = (100, -1))
        self.startBtn.SetFont(font = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        self.startBtn.SetForegroundColour(wx.WHITE)
        
        #binds start button with function onstart
        self.startBtn.Bind(wx.EVT_BUTTON, self.onstart)
        
        self.instructionpanel = wx.Panel(self)
        self.instructionpanel.SetFont(wx.Font(20, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        
        self.patientdetailpanel = wx.Panel(self)
        self.patientdetailpanel.SetFont(wx.Font(16, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        
        self.PatientDetailsText = wx.StaticText(self.patientdetailpanel, label = "Patient's Details:")
        self.PatientDetailsText.SetFont(wx.Font(30, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.PatientDetailsText.SetForegroundColour(wx.WHITE)
        
        self.SubjectNameText = wx.StaticText(self.patientdetailpanel, label = "Name:")
        self.SubjectNameText.SetForegroundColour(wx.WHITE)
        self.SubjectNameEditable = wx.TextCtrl(self.patientdetailpanel)
        self.SubjectNameEditable.SetBackgroundColour(wx.Colour(50, 50, 50))
        self.SubjectNameEditable.SetForegroundColour(wx.WHITE)
        
        self.SubjectIdNumText = wx.StaticText(self.patientdetailpanel, label = "Subject Id:")
        self.SubjectIdNumText.SetForegroundColour(wx.WHITE)
        self.SubjectIdNumEditable = wx.TextCtrl(self.patientdetailpanel)
        self.SubjectIdNumEditable.SetBackgroundColour(wx.Colour(50, 50, 50))
        self.SubjectIdNumEditable.SetForegroundColour(wx.WHITE) 
        
        self.AgeText = wx.StaticText(self.patientdetailpanel, label = "Age (yrs):")
        self.AgeText.SetForegroundColour(wx.WHITE)
        self.AgeEditable = wx.TextCtrl(self.patientdetailpanel, size = (45, -1), validator = MyValidator())
        self.AgeEditable.SetMaxLength(2)
        self.AgeEditable.SetFont(wx.Font(16, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.AgeEditable.SetBackgroundColour(wx.Colour(50, 50, 50))
        self.AgeEditable.SetForegroundColour(wx.WHITE)
        
        self.GenderText = wx.StaticText(self.patientdetailpanel, label = "Gender:")
        self.GenderText.SetForegroundColour(wx.WHITE)
        self.GenderEditable = wx.ComboBox(self.patientdetailpanel, choices = ["M", "F"], style = wx.CB_READONLY)
        self.GenderEditable.SetFont(wx.Font(16, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)) 
        
        self.InjuryTypeText = wx.StaticText(self.patientdetailpanel, label = "Injury Type:")
        self.InjuryTypeText.SetForegroundColour(wx.WHITE)
        self.InjuryTypeEditable = wx.ComboBox(self.patientdetailpanel, choices = ["Paraplegia", "Tetraplegia"], style = wx.CB_READONLY)
        self.InjuryTypeEditable.SetFont(wx.Font(16, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        
        self.GroupText = wx.StaticText(self.patientdetailpanel, label = "Group:")
        self.GroupText.SetForegroundColour(wx.WHITE)
        self.GroupEditable = wx.TextCtrl(self.patientdetailpanel, size = (100, -1), validator = MyValidator())
        self.GroupEditable.SetBackgroundColour(wx.Colour(50, 50, 50))
        self.GroupEditable.SetForegroundColour(wx.WHITE)
        
        self.PainText = wx.StaticText(self.patientdetailpanel, label = "Pain Score:")
        self.PainText.SetForegroundColour(wx.WHITE)
        self.PainEditable = wx.TextCtrl(self.patientdetailpanel, size = (100, -1), validator = MyValidator())
        self.PainEditable.SetBackgroundColour(wx.Colour(50, 50, 50))
        self.PainEditable.SetForegroundColour(wx.WHITE)
        
        self.InstructionTitle = wx.StaticText(self.instructionpanel)
        if self.Parent.english.IsChecked():
            self.InstructionTitle.SetLabel("Instructions:")
            self.startBtn.SetLabel('Start')
            self.Heading.SetLabel('Laterality Training Module')            
        else:
            self.InstructionTitle.SetLabel("निर्देश-")
            self.startBtn.SetLabel('प्रारंभ')
            self.Heading.SetLabel('पार्श्वता प्रशिक्षण मॉड्यूल')
        self.InstructionTitle.SetForegroundColour(wx.WHITE)
        self.InstructionTitle.SetFont(wx.Font(25, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        
        self.Instructions = wx.StaticText(self.instructionpanel)
        
        if self.Parent.click.IsChecked() and self.Parent.english.IsChecked():
            txt = self.Parent.onclickeng()
        elif self.Parent.click.IsChecked() and self.Parent.hindi.IsChecked():
            txt = self.Parent.onclickhin()
        elif self.Parent.hover.IsChecked() and self.Parent.english.IsChecked():
            txt = self.Parent.onhovereng()
        else:
            txt = self.Parent.onhoverhin()        
        
        self.Instructions.SetLabel(txt)
        self.Instructions.SetForegroundColour(wx.WHITE)
        
        PHSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        PHSizer1.Add(self.SubjectNameText, 0, wx.CENTRE | wx.LEFT, 5)
        PHSizer1.AddSpacer(65)
        PHSizer1.Add(self.SubjectNameEditable, 1, wx.CENTRE | wx.RIGHT, 5)
        
        PHSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        PHSizer2.Add(self.SubjectIdNumText, 0, wx.CENTRE | wx.LEFT, 5)
        PHSizer2.AddSpacer(32)
        PHSizer2.Add(self.SubjectIdNumEditable, 1, wx.CENTRE | wx.RIGHT, 5)
        
        PHSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        PHSizer3.Add(self.AgeText, 0, wx.CENTRE | wx.LEFT, 5)
        PHSizer3.AddSpacer(40)
        PHSizer3.Add(self.AgeEditable, 1, wx.CENTRE | wx.RIGHT, 5)
        
        PHSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        PHSizer4.Add(self.GenderText, 0, wx.CENTRE | wx.LEFT, 5)
        PHSizer4.AddSpacer(55)
        PHSizer4.Add(self.GenderEditable, 1, wx.CENTRE | wx.RIGHT, 5)
        
        PHSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        PHSizer5.Add(self.InjuryTypeText, 0, wx.CENTRE | wx.LEFT, 5)
        PHSizer5.AddSpacer(21)
        PHSizer5.Add(self.InjuryTypeEditable, 1, wx.CENTRE | wx.RIGHT, 5)
        
        PHSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        PHSizer6.Add(self.GroupText, 0, wx.CENTRE | wx.LEFT, 5)
        PHSizer6.AddSpacer(60)
        PHSizer6.Add(self.GroupEditable, 1, wx.CENTRE | wx.RIGHT, 5)        
        
        PHSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        PHSizer7.Add(self.PainText, 0, wx.CENTRE | wx.LEFT, 5)
        PHSizer7.AddSpacer(25)
        PHSizer7.Add(self.PainEditable, 1, wx.CENTRE | wx.RIGHT, 5)
        
        PVSizer1 = wx.BoxSizer(wx.VERTICAL)
        PVSizer1.AddStretchSpacer()
        PVSizer1.Add(self.PatientDetailsText, 0, wx.CENTRE)
        PVSizer1.AddSpacer(10)
        PVSizer1.Add(PHSizer1, 0, wx.EXPAND)
        PVSizer1.AddSpacer(10)
        PVSizer1.Add(PHSizer2, 0, wx.EXPAND)
        PVSizer1.AddSpacer(10)
        PVSizer1.Add(PHSizer3)
        PVSizer1.AddSpacer(10)
        PVSizer1.Add(PHSizer4)
        PVSizer1.AddSpacer(10)
        PVSizer1.Add(PHSizer5)
        PVSizer1.AddSpacer(10)
        PVSizer1.Add(PHSizer6)        
        PVSizer1.AddSpacer(10)
        PVSizer1.Add(PHSizer7)        
        PVSizer1.AddStretchSpacer()
        self.patientdetailpanel.SetSizer(PVSizer1)        
        
        VSizer = wx.BoxSizer(wx.VERTICAL)
        VSizer.AddStretchSpacer()
        VSizer.Add(self.InstructionTitle, 0, wx.LEFT, 10)
        VSizer.AddSpacer(10)
        VSizer.Add(self.Instructions, 0, wx.LEFT, 10)
        VSizer.AddStretchSpacer()        
        self.instructionpanel.SetSizer(VSizer)
        
        HSizer = wx.BoxSizer(wx.HORIZONTAL)
        HSizer.Add(self.patientdetailpanel, 1, wx.EXPAND)
        HSizer.Add((wx.StaticLine(self, style = wx.LI_VERTICAL)), 0, wx.EXPAND)
        HSizer.Add(self.instructionpanel, 2, wx.EXPAND)
        
        MainSizer = wx.BoxSizer(wx.VERTICAL)
        MainSizer.AddSpacer(10)
        MainSizer.Add(self.Heading, 0, wx.ALIGN_CENTER)
        MainSizer.AddSpacer(10)
        MainSizer.Add(HSizer, 1, wx.EXPAND)
        MainSizer.AddSpacer(10)
        MainSizer.Add(self.startBtn, 0, wx.ALIGN_CENTER)
        MainSizer.AddSpacer(10)
        self.SetSizer(MainSizer)
    
    
    
    def onstart(self, event):
        #showing setpanel(SetPanel)
        self.Parent.mainsizer.Hide(0)
        self.Parent.mainsizer.Show(1)  
        self.Parent.setpanel.SetFocus()
        
        self.Parent.mainsizer.Layout()
        self.Parent.setpanel.Layout()
        
        #starting timer for which the panel will be displayed 
        #it'll call the function every 1000 milli sec, or 1 sec
        self.Parent.setpanel.timer.Start(1000)
        
class MyValidator(wx.Validator):
    def __init__(self):
        wx.Validator.__init__(self)
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self):
        return MyValidator()

    def OnChar(self, event):
        key = event.GetKeyCode()

        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            event.Skip()
            return

        if chr(key) in string.digits:
            event.Skip()
            return

        if not wx.Validator.IsSilent():
            wx.Bell()

        # Returning without calling even.Skip eats the event before it
        # gets to the text control
        return

#panel for set number page        
class SetPanel(wx.Panel):
    def __init__ (self,parent, *args,**kwargs):
        super().__init__(parent, *args,**kwargs)
        
        self.SetBackgroundColour((20, 20, 20))
        
        #declaration of variables
        #set number
        self.set_num = 1    
        #time for which the set panel is visible (sec), 5 secs only for testing 
        self.timeToLive = 5
        
        #declaration of sizer
        sizer=wx.BoxSizer(wx.VERTICAL)
        
        #text on the panel
        self.timemsg = wx.StaticText(self, -1)
        self.timemsg.SetFont(font = wx.Font(30, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        self.timemsg.SetForegroundColour(wx.WHITE)
        
        self.lbl = wx.StaticText(self,-1,style = wx.ALIGN_CENTER)
        font = wx.Font(30, wx.ROMAN, wx.NORMAL, wx.NORMAL)
        self.lbl.SetForegroundColour(wx.WHITE)
        
        #string of set number, set_num stores set number
        if self.Parent.english.IsChecked():
            txt = "SET {}".format(str(self.set_num))
            timetxt = "Starting test in {}s...".format(self.timeToLive)
        else:
            txt = "सेट {}".format(str(self.set_num))
            timetxt = "परीक्षा शुरू होने में {} सेकंड बाकि".format(self.timeToLive) 
        self.lbl.SetFont(font)        
        self.lbl.SetLabel(txt)
        self.timemsg.SetLabel(timetxt)
        
        #incrimenting set number
        self.set_num += 1
        
        #adding texts in sizer
        sizer.AddStretchSpacer()
        sizer.Add(self.lbl,0 , wx.ALIGN_CENTER)
        sizer.AddStretchSpacer()
        sizer.Add(self.timemsg, 0, wx.ALIGN_CENTER)
        sizer.AddStretchSpacer()
        self.SetSizer(sizer)
        
        #binding timer with ontimer function
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onTimer, self.timer)
        
    def onTimer(self, evt):
        #function is called every 1 sec, so this will decrease time remaining by 1 sec every time ontimer function is called
        self.timeToLive -= 1
        #responsible for desplaying time remaining every sec on the panel
        if self.Parent.english.IsChecked():
            self.timemsg.SetLabel("Starting test in {}s...".format(self.timeToLive))
        else:
            self.timemsg.SetLabel("परीक्षा शुरू होने में {} सेकंड बाकि".format(self.timeToLive))
        
        #when time remaining becomes 0
        if self.timeToLive == 0:
            #timer is stopped
            self.timer.Stop()
            
            #showing setpanel (PhotoPanel)
            self.Parent.nextpanel.nextpanel = 2
            self.Parent.mainsizer.Hide(1)
            self.Parent.mainsizer.Show(4)
            self.Parent.nextpanel.SetFocus()
            self.Parent.mainsizer.Layout()
            self.Parent.nextpanel.Layout()
           
#main panel which displays all the pictures and left, right buttons       
class PhotoPanel(wx.Panel):
    def __init__ (self, parent, *args, **kwargs):
        super().__init__(parent, *args,**kwargs)
        
        self.ImgNum = []
        self.num = 0                                                           #stores the picture number index 
        self.responselist = []                                                 #ImgNum for responses from all sets 
        self.responses = []                                                    #ImgNum for responses from a particular set
        self.resptime = 0                                                      #for storing response time of a particular picture, declared separately as we are using time.time()                                             
        self.CorrectResponseCount = 0
        self.InCorrectResponseCount = 0
        self.NoResponseCount = 0
        self.AllowBtnClick = True
        
        for i in range(1, 25):
            self.ImgNum.append(str(i))                                         #ImgNum to store names of pictures, 10 pictures for testing only
        self.Resize = False
        
        random.shuffle(self.ImgNum)                                            #shuffles the elements of ImgNum, different every time         
        
        #left, right buttons
        self.leftBtn = GradientButton(self, wx.NewId())
        self.leftBtn.SetFont(wx.Font(30, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        self.leftBtn.SetForegroundColour(wx.WHITE)
        self.rightBtn = GradientButton(self, wx.NewId()) 
        self.rightBtn.SetFont(wx.Font(30, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        self.rightBtn.SetForegroundColour(wx.WHITE)
        
        if self.Parent.english.IsChecked():
            self.rightBtn.SetLabel('RIGHT')
            self.leftBtn.SetLabel('LEFT')
        else:
            self.rightBtn.SetLabel('दाएं')
            self.leftBtn.SetLabel('बाएं')
        
        self.ImagePanel = wx.Panel(self)
        self.ImagePanel.SetBackgroundColour((20, 20, 20))
        
        self.hsizer=wx.BoxSizer(wx.HORIZONTAL)        
        
        #binding buttons to their functions
        if self.Parent.click.IsChecked():
            self.leftBtn.Bind(wx.EVT_BUTTON, self.onleft)
            self.rightBtn.Bind(wx.EVT_BUTTON, self.onright)
            
        else:
            self.leftBtn.Bind(wx.EVT_MOTION, self.onleft)
            self.rightBtn.Bind(wx.EVT_MOTION, self.onright)                        
            
        self.w = self.h = 0
        self.CurBmp = wx.Bitmap(0, 0)
        
        #adding image and buttons in sizers
        self.hsizer.Add(self.leftBtn, 1, wx.EXPAND)
        
        self.hsizer.Add(self.ImagePanel, 3, wx.EXPAND)
        
        self.hsizer.Add(self.rightBtn, 1, wx.EXPAND)                
        self.SetSizer(self.hsizer)
        
        #time limit for each picture
        self.timer = wx.Timer(self)
        self.timeToLive = 5                                         #time for displaying each picture
        self.Bind(wx.EVT_TIMER, self.onTimer, self.timer)           #binding timer to ontimer function
        
        self.ImagePanel.Timer = wx.Timer(self.ImagePanel)
        self.ImagePanel.Bind(wx.EVT_TIMER, self.OnImagePanelTimer, self.ImagePanel.Timer)
        
        #Binding size and idle event
        self.ImagePanel.Bind(wx.EVT_PAINT, self.OnPaint)
        self.ImagePanel.Bind(wx.EVT_SIZE, self.OnSize)
        self.ImagePanel.Bind(wx.EVT_IDLE, self.OnIdle)
        
        self.sw, self.sh = self.ImagePanel.GetSize()

        
    def OnPaint(self, event):
        dc = wx.PaintDC(self.ImagePanel)
        dc.DrawBitmap(self.CurBmp, int((self.ImagePanel.GetSize()[0] - self.w) / 2), int((self.ImagePanel.GetSize()[1] - self.h) / 2))
        
    def OnSize(self, event):
        self.Resize = True
        event.Skip()
    
    def OnIdle(self, event):
        if self.Resize:
            self.SettingImage()            
        self.Resize = False
        
    def SettingImage(self):
        self.sw, self.sh = self.ImagePanel.GetSize()
        if self.sw and self.sh:
            self.Img = wx.Image(r"images/" + self.ImgNum[self.num]+'.jpg', wx.BITMAP_TYPE_ANY)
            self.fw, self.fh = self.Img.GetSize()
            self.w, self.h = self.ScaleFrame(self.fw, self.fh, self.sw, self.sh)      #calls function scale frame which returns the required size
            self.Img.Rescale(self.w, self.h)
            self.CurBmp = self.Img.ConvertToBitmap()
            self.ImagePanel.Refresh()
            wx.YieldIfNeeded() 
    
    def onTimer(self, evt):
        #decreases timetolive by 1 sec every time it is called (every 1 sec)
        self.timeToLive -= 1            
        
        #if time limit for a picture ends
        if self.timeToLive == 0:         
            #if self.Parent.photopanel.leftBtn.HasFocus() or self.Parent.photopanel.rightBtn.HasFocus():
                #win32api.SetCursorPos(((self.Parent.GetSize()[0] + self.Parent.GetPosition()[0])//2, (self.Parent.GetSize()[1] + self.Parent.GetPosition()[1])//2))
                
            if int(self.ImgNum[self.num]) % 2 == 0:
                self.responses.append(("L", " ", 5))
            else:
                self.responses.append(("R", " ", 5))
             
            self.NoResponseCount += 1
               
            #calls function NextPhoto which handles further processes, common to all three responses (left,right,NR)    
            self.NextPhoto()                
                            
            
    #called when response is left    
    def onleft(self, e):
        if self.AllowBtnClick:
            #if self.Parent.photopanel.leftBtn.HasFocus() or self.Parent.photopanel.rightBtn.HasFocus():
                #win32api.SetCursorPos(((self.Parent.GetSize()[0] + self.Parent.GetPosition()[0])//2, (self.Parent.GetSize()[1] + self.Parent.GetPosition()[1])//2))
            
            self.AllowBtnClick = False
            
            self.resptime = time.time() - self.resptime         #calculates response time as time.time() returns current time and self.resptime stored time when a particulare picture was shown
            if int(self.ImgNum[self.num]) % 2 == 0:
                self.responses.append(("L", "L", self.resptime))    
                self.DrawSymbol(True)
            else:
                self.responses.append(("R", "L", self.resptime))
                self.DrawSymbol(False)
            
            self.ImagePanel.Timer.Start(1000)
        
    
    #everything same as onleft
    def onright(self, e):
        if self.AllowBtnClick:
            #if self.Parent.photopanel.leftBtn.HasFocus() or self.Parent.photopanel.rightBtn.HasFocus():
                #win32api.SetCursorPos(((self.Parent.GetSize()[0] + self.Parent.GetPosition()[0])//2, (self.Parent.GetSize()[1] + self.Parent.GetPosition()[1])//2))
            
            self.AllowBtnClick = False
            
            self.resptime = time.time() - self.resptime
            if int(self.ImgNum[self.num]) % 2 == 0:
                self.responses.append(("L", "R", self.resptime))
                self.DrawSymbol(False)
            else:
                self.responses.append(("R", "R", self.resptime))
                self.DrawSymbol(True)
                
            self.ImagePanel.Timer.Start(1000)
        
    def DrawSymbol(self, Symbol):
        dc = wx.ClientDC(self.ImagePanel)
        #dc = wx.BufferedDC(dc, self.CurBmp)
        dc = wx.GCDC(dc)        
        
        if Symbol:
            dc.SetPen(wx.Pen((0, 255, 0), 30, wx.PENSTYLE_SOLID))
            dc.DrawLine(0.2 * self.sw, 0.5 * self.sh, 0.3 * self.sw, 0.7 * self.sh)
            dc.DrawLine(0.8 * self.sw, 0.3 * self.sh, 0.3 * self.sw, 0.7 * self.sh)
            self.CorrectResponseCount += 1
            #print(self.CorrectResponseCount)
        else:
            dc.SetPen(wx.Pen((255, 0, 0), 30, wx.PENSTYLE_SOLID))
            dc.DrawLine(0.2 * self.sw, 0.2 * self.sh, 0.8 * self.sw, 0.8 * self.sh)
            dc.DrawLine(0.2 * self.sw, 0.8 * self.sh, 0.8 * self.sw, 0.2 * self.sh)        
            self.InCorrectResponseCount += 1
            #print(self.InCorrectResponseCount)
            
        #self.Refresh()            
        
    def OnImagePanelTimer(self, event):
        self.ImagePanel.Timer.Stop()
        if not self.leftBtn.IsEnabled():
            self.leftBtn.Enable(True)
        if not self.rightBtn.IsEnabled():
            self.rightBtn.Enable(True)
        self.NextPhoto()
    
    #handles all processes required to put up next picture in order, common for all three responses
    def NextPhoto(self):                                    
        self.timer.Stop()           #stops the timer (5 sec)
        self.num += 1                 #incriments the picture number index
        
        if self.num <= 23:                                                               #if picture number index is valid, 9 as we are initially testing with 10 pictures
            self.SettingImage()
            self.timer = wx.Timer(self)
            self.Parent.nextpanel.nextpanel = 1
            self.resptime = time.time()                                                 #for recording the response time, it stores the current time when the picture is displayed, and later when a response comes it can be subtracted from time.time() to get the response time                        
            self.Parent.mainsizer.Hide(2)
            self.Parent.mainsizer.Show(4)
            self.Parent.nextpanel.SetFocus()
            self.Parent.mainsizer.Layout()
            self.Parent.nextpanel.Layout()            
        else:                                                                           #operates when a particular set gets completed            
            self.responselist.append(self.responses)                                    #appends responses of a particular set 
            if self.Parent.setpanel.set_num == 2:                                       #(only for testing) if it is the last set, then print the response ImgNum, and response time ImgNum and close the window 
                #print(self.responselist)
                
                self.Parent.mainsizer.Hide(2)
                
                self.Parent.endpanel.CorrectResult.SetLabel(str(self.Parent.photopanel.CorrectResponseCount))
                self.Parent.endpanel.InCorrectResult.SetLabel(str(self.Parent.photopanel.InCorrectResponseCount))
                self.Parent.endpanel.NoResponseResult.SetLabel(str(self.Parent.photopanel.NoResponseCount))
                
                self.Parent.mainsizer.Show(3)
                self.Parent.endpanel.SetFocus()
                self.Parent.mainsizer.Layout()
                
            else:
                #shuffles the ImgNum after every set           
                random.shuffle(self.ImgNum)
        
                #first picture of next set
                self.num = 0
                self.SettingImage()
                #same as inside photo panel
                self.Parent.setpanel.timeToLive = 5
                #timetxt = 'Starting test in %ds...'%self.Parent.setpanel.timeToLive
                #self.Parent.setpanel.timemsg.SetLabel(timetxt)
                if self.Parent.english.IsChecked():
                    self.Parent.setpanel.timemsg.SetLabel("Starting test in {}s...".format(self.Parent.setpanel.timeToLive))
                    self.Parent.setpanel.lbl.SetLabel("SET {}".format(str(self.Parent.setpanel.set_num)))
                else:
                    self.Parent.setpanel.timemsg.SetLabel("परीक्षा शुरू होने में {} सेकंड बाकि".format(self.Parent.setpanel.timeToLive))
                    self.Parent.setpanel.lbl.SetLabel("सेट {}".format(str(self.Parent.setpanel.set_num)))
                self.Parent.setpanel.set_num += 1
                self.Parent.mainsizer.Hide(2)
                self.Parent.mainsizer.Show(1)  
                self.Parent.setpanel.SetFocus()
                self.Parent.mainsizer.Layout()
                self.Parent.setpanel.Layout()
                self.Parent.setpanel.timer.Start(1000)
        #print(self.num, self.Parent.setpanel.set_num, "self.num")                    
        self.AllowBtnClick = True      
    
    #function to return size in which photo should be rescaled
    def ScaleFrame(self, fw, fh, sw, sh):
        if sw < sh:
            fh = (fh * sw) / fw
            fw = sw
            if fh > sh:
                fw = (fw * sh) / fh
                fh = sh
        else:
            fw = (fw * sh) / fh
            fh = sh
            if fw > sw:
                fh = (fh * sw) / fw
                fw = sw
        self.CurSize = (int(fw), int(fh))
        return (int(fw), int(fh))
    
class EndPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour((20, 20, 20))
        
        Heading = wx.StaticText(self, label = "Training Complete")
        Heading.SetFont(font = wx.Font(40, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        Heading.SetForegroundColour(wx.WHITE)
        
        CorrectResultText = wx.StaticText(self, label = "Number of correct responses: ")
        CorrectResultText.SetFont(font = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        CorrectResultText.SetForegroundColour(wx.WHITE)
        
        self.CorrectResult = wx.StaticText(self, label = "")
        self.CorrectResult.SetFont(font = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        self.CorrectResult.SetForegroundColour(wx.WHITE)   
        
        InCorrectResultText = wx.StaticText(self, label = "Number of incorrect responses: ")
        InCorrectResultText.SetFont(font = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        InCorrectResultText.SetForegroundColour(wx.WHITE)
        
        self.InCorrectResult = wx.StaticText(self, label = "")
        self.InCorrectResult.SetFont(font = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        self.InCorrectResult.SetForegroundColour(wx.WHITE)         
        
        NoResponseResultText = wx.StaticText(self, label = "Number of no responses: ")
        NoResponseResultText.SetFont(font = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        NoResponseResultText.SetForegroundColour(wx.WHITE)
        
        self.NoResponseResult = wx.StaticText(self, label = "")
        self.NoResponseResult.SetFont(font = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        self.NoResponseResult.SetForegroundColour(wx.WHITE)        
        
        #declaration of save button
        SaveBtn = GradientButton(self, wx.NewId(), label='Save', size = (100, -1))        
        SaveBtn.SetFont(font = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        SaveBtn.SetForegroundColour(wx.WHITE)
        
        #declaration of Restart button
        RestartBtn = GradientButton(self, wx.NewId(), label='Restart', size = (100, -1))        
        RestartBtn.SetFont(font = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        RestartBtn.SetForegroundColour(wx.WHITE)
        
        HSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        HSizer1.Add(CorrectResultText)
        HSizer1.AddSpacer(10)
        HSizer1.Add(self.CorrectResult)
        
        HSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        HSizer2.Add(InCorrectResultText)
        HSizer2.AddSpacer(10)
        HSizer2.Add(self.InCorrectResult)
        
        HSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        HSizer3.Add(NoResponseResultText)
        HSizer3.AddSpacer(10)
        HSizer3.Add(self.NoResponseResult)
        
        HSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        HSizer4.Add(SaveBtn, 1)
        HSizer4.AddStretchSpacer()
        HSizer4.Add(RestartBtn, 1)
        
        VSizer = wx.BoxSizer(wx.VERTICAL)
        VSizer.AddSpacer(10)
        VSizer.Add(Heading, 0, wx.CENTER)
        VSizer.AddStretchSpacer()
        VSizer.Add(HSizer1, 0, wx.CENTER)
        VSizer.AddSpacer(10)
        VSizer.Add(HSizer2, 0, wx.CENTER)
        VSizer.AddSpacer(10)
        VSizer.Add(HSizer3, 0, wx.CENTER)
        VSizer.AddStretchSpacer()
        VSizer.Add(HSizer4, 1, wx.CENTER)
        VSizer.AddSpacer(10)        
        self.SetSizer(VSizer)
        
        SaveBtn.Bind(wx.EVT_BUTTON, self.OnSave)
        RestartBtn.Bind(wx.EVT_BUTTON, self.OnRestart)
        
    def OnSave(self, event):
        Dlg = wx.FileDialog(self, message="Choose a file to save", wildcard = "Excel 97-2003 Workbook (*.xls)|*.xls",
                            style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        
        if Dlg.ShowModal() == wx.ID_OK:
            try:
                LoadPath = Dlg.GetPath()
                self.ActualSaving(LoadPath)
            except:
                if hasattr(self, "DlgWithGauge"):
                    self.DlgWithGauge.MakeModal(False)
                    self.DlgWithGauge.Destroy()
                Dlg = Dialog(self, -1, "Error")
                Dlg.ErrorDialog()
                Dlg.CentreOnScreen()
                Dlg.Show()
                Dlg.MakeModal(True)
            
    def ActualSaving(self, LoadPath):
        self.DlgWithGauge = Dialog(self, -1, "Save")
        self.DlgWithGauge.DialogWithGauge("Saving File")
        self.DlgWithGauge.CenterOnScreen()
        self.DlgWithGauge.Show()
        self.DlgWithGauge.MakeModal(True)
        
        self.DlgWithGauge.Gauge.SetValue(5)
        self.DlgWithGauge.Gauge.Refresh()
        wx.Yield()        
        
        wb = xlwt.Workbook()
        
        ws = wb.add_sheet("Patient's Details")
        ws.write(0, 0, "Subject's Name")
        ws.write(0, 1, self.Parent.initialpanel.SubjectNameEditable.GetValue())
        ws.write(1, 0, "Subject's Id")
        ws.write(1, 1, self.Parent.initialpanel.SubjectIdNumEditable.GetValue())
        ws.write(2, 0, "Age")
        ws.write(2, 1, self.Parent.initialpanel.AgeEditable.GetValue())
        ws.write(3, 0, "Gender")
        ws.write(3, 1, self.Parent.initialpanel.GenderEditable.GetValue())
        ws.write(4, 0, "Type of Injury")
        ws.write(4, 1, self.Parent.initialpanel.InjuryTypeEditable.GetValue())
        ws.write(5, 0, "Group")
        ws.write(5, 1, self.Parent.initialpanel.GroupEditable.GetValue())
        ws.write(6, 0, "Pain")
        ws.write(6, 1, self.Parent.initialpanel.PainEditable.GetValue())
        
        self.DlgWithGauge.Gauge.SetValue(20)
        self.DlgWithGauge.Gauge.Refresh()
        wx.Yield()
        time.sleep(0.3)
        
        TotalSum = 0
        CorrectResponseSum = 0
        
        Mul = 90 / len(self.Parent.photopanel.responselist)
        
        for i in range(len(self.Parent.photopanel.responselist)):
            ws = wb.add_sheet("Set " + str(i + 1))
            ws.write(0, 0, "Correct Value")
            ws.write(0, 1, "Subject's Response")
            ws.write(0, 2, "Time")
            for j in range(len(self.Parent.photopanel.responselist[i])):
                ws.write(j + 1, 0, self.Parent.photopanel.responselist[i][j][0])
                ws.write(j + 1, 1, self.Parent.photopanel.responselist[i][j][1])
                ws.write(j + 1, 2, self.Parent.photopanel.responselist[i][j][2])
                if self.Parent.photopanel.responselist[i][j][0] == self.Parent.photopanel.responselist[i][j][1]:
                    CorrectResponseSum += self.Parent.photopanel.responselist[i][j][2]
                TotalSum += self.Parent.photopanel.responselist[i][j][2]
                
            self.DlgWithGauge.Gauge.SetValue(20 + Mul * i)
            self.DlgWithGauge.Gauge.Refresh()
            wx.Yield()            
        
        ws = wb.get_sheet(0)
        ws.write(8, 0, "Total Mean Time (seconds)")
        #print(TotalSum, self.Parent.setpanel.set_num, self.Parent.photopanel.num, "Total Time")
        ws.write(8, 1, TotalSum / ((self.Parent.photopanel.num) * (self.Parent.setpanel.set_num - 1)))
        
        ws.write(9, 0, "Total Mean Time for Correct Responses (seconds)")
        ws.write(11, 0, 'Number of Correct Responses:')
        ws.write(12, 0, 'Number of Incorrect Responses:')
        ws.write(13, 0, 'Number of No Responses:')
        ws.write(11, 1, self.Parent.photopanel.CorrectResponseCount)
        ws.write(12, 1, self.Parent.photopanel.InCorrectResponseCount)
        ws.write(13, 1, self.Parent.photopanel.NoResponseCount)
        if self.Parent.photopanel.CorrectResponseCount:
            ws.write(9, 1, CorrectResponseSum / self.Parent.photopanel.CorrectResponseCount)
        
        wb.save(LoadPath)            
        
        self.DlgWithGauge.Heading.SetLabel("Report Generation Complete")
        self.DlgWithGauge.sizer.Layout()
        self.DlgWithGauge.Gauge.SetValue(100)
        self.DlgWithGauge.Gauge.Refresh()
        wx.Yield()        
        time.sleep(0.3)
        
        self.DlgWithGauge.MakeModal(False)
        self.DlgWithGauge.Destroy()
        
        
    def OnRestart(self, event):
        #shuffles the ImgNum after every set           
        random.shuffle(self.Parent.photopanel.ImgNum)
        
        #Initialising Pateint's Details
        self.Parent.initialpanel.SubjectNameEditable.SetLabel("")
        self.Parent.initialpanel.SubjectIdNumEditable.SetLabel("")
        self.Parent.initialpanel.AgeEditable.SetLabel("")
        self.Parent.initialpanel.GenderEditable.SetSelection(-1)
        self.Parent.initialpanel.InjuryTypeEditable.SetSelection(-1)
        self.Parent.initialpanel.GroupEditable.SetLabel("")
        self.Parent.initialpanel.PainEditable.SetLabel("")
        
        
        #first picture of next set
        self.Parent.photopanel.num = 0                                                           #stores the picture number index 
        self.Parent.photopanel.responselist = []                                                 #ImgNum for responses from all sets 
        self.Parent.photopanel.responses = []                                                    #ImgNum for responses from a particular set 
        self.Parent.photopanel.resptime = 0                                                      #for storing response time of a particular picture, declared separately as we are using time.time()
        self.Parent.photopanel.CorrectResponseCount = 0
        self.Parent.photopanel.InCorrectResponseCount = 0
        self.Parent.photopanel.NoResponseCount = 0
        self.Parent.photopanel.AllowBtnClick = True
        
        self.Parent.photopanel.SettingImage()
        #same as inside photo panel
        self.Parent.setpanel.set_num = 1
        self.Parent.setpanel.timeToLive = 5
        if self.Parent.english.IsChecked():
            txt = "SET {}".format(str(self.Parent.setpanel.set_num))
            timetxt = "Starting test in {}s...".format(self.Parent.setpanel.timeToLive)
        else:
            txt = "सेट {}".format(str(self.Parent.setpanel.set_num))
            timetxt = "परीक्षा शुरू होने में {} सेकंड बाकि".format(self.Parent.setpanel.timeToLive)
        
        self.Parent.setpanel.lbl.SetLabel(txt)
        self.Parent.setpanel.timemsg.SetLabel(timetxt)
        self.Parent.setpanel.set_num += 1
        
        self.Parent.mainsizer.Hide(3)
        self.Parent.mainsizer.Show(0)  
        self.Parent.setpanel.SetFocus()
        self.Parent.mainsizer.Layout()
        
class Dialog(wx.Frame):
    def __init__(self, parent, id, title, size=wx.DefaultSize,
                 pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE, name='dialog'):
        wx.Dialog.__init__(self)
        self.Create(parent, id, title, pos, size, style, name)
        self.SetBackgroundColour(wx.Colour(20, 20, 20))
        
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        
    def DialogWithGauge(self, Heading):
        
        self.Heading = wx.StaticText(self, -1, label = Heading)
        self.Heading.SetFont(wx.Font(12, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.Heading.SetForegroundColour(wx.WHITE)

        self.Gauge = PG.PyGauge(self, -1, range = 100, size = (300, 20), style=wx.GA_HORIZONTAL)
        self.Gauge.SetValue(0)
        self.Gauge.SetBackgroundColour(wx.WHITE)
        self.Gauge.SetBorderColor((26, 170, 26))
        self.Gauge.SetBarColor((26, 170, 26))

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.AddSpacer(10)
        self.sizer.Add(self.Heading, 1, wx.CENTER)
        self.sizer.Add(self.Gauge, 0, wx.CENTER | wx.ALL, 10)
        self.sizer.AddSpacer(10)
        self.SetSizer(self.sizer)
        self.Fit()
        
    def ErrorDialog(self):
        global Error
        
        self.Content = wx.StaticText(self, label = "There is an error while generating the report. \n Please try again. \n Possible reason includes: \n  1.Excel file is already opened. \n  2.Saving Excel file where you don't have write permission. \n If problem persists contact your Auptimo representative.")
        self.Content.SetFont(font = wx.Font(14, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        self.Content.SetForegroundColour(wx.WHITE)
        
        self.Logo = wx.StaticBitmap(self, bitmap = Error.GetBitmap())
        
        self.HSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.HSizer.AddSpacer(10)
        self.HSizer.Add(self.Logo, 0, wx.TOP, 20)
        self.HSizer.Add(self.Content, 0, wx.CENTER | wx.ALL, 15)
        self.SetSizer(self.HSizer)
        self.Fit()
        
    def MakeModal(self, modal=True):
        if modal and not hasattr(self, '_disabler'):
            self._disabler = wx.WindowDisabler(self)
        if not modal and hasattr(self, '_disabler'):
            del self._disabler 
            
    def OnClose(self, event):
        self.MakeModal(False)
        self.Destroy()
        
class MySplashScreen(SplashScreen):
    def __init__(self):
        global SplashScreenImg
        SplashScreen.__init__(self, SplashScreenImg.GetBitmap(),
                                 wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
                                 4000, None, -1)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.fc = wx.CallLater(3000, self.ShowMain)


    def OnClose(self, event):
        # Make sure the default handler runs too so this window gets
        # destroyed
        event.Skip()
        self.Hide()        
        
        # if the timer is still running then go ahead and show the
        # main frame now
        if self.fc.IsRunning():
            self.fc.Stop()
            self.ShowMain()        
        
    def ShowMain(self):
        frame = Frame(None)         #instance of class frame
        frame.Show()
        frame.Maximize(maximize=True)
         
class nextpanel(wx.Panel):
    def __init__ (self,parent, *args,**kwargs):
        super().__init__(parent, *args,**kwargs)
        
        self.SetBackgroundColour((20, 20, 20))
        sizer=wx.BoxSizer(wx.HORIZONTAL)
        sizer.AddStretchSpacer(4)
        self.nextbtn = GradientButton(self, wx.NewId())
        self.nextbtn.SetForegroundColour(wx.WHITE)
        if self.Parent.click.IsChecked():
            self.nextbtn.Unbind(wx.EVT_MOTION, None)
            self.nextbtn.Bind(wx.EVT_BUTTON, self.onnext)
        else:
            self.nextbtn.Unbind(wx.EVT_BUTTON, None)
            self.nextbtn.Bind(wx.EVT_MOTION, self.onnext)
        if self.Parent.english.IsChecked():
            self.nextbtn.SetLabel('Next')
        else:
            self.nextbtn.SetLabel('अगला')
        self.nextbtn.SetFont(wx.Font(30, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        sizer.Add(self.nextbtn, 2, wx.EXPAND)
        sizer.AddStretchSpacer(4)
        self.SetSizer(sizer)
        self.nextpanel = 0
    
    def onnext(self, e):
        
        if self.nextpanel == 1:
            self.Parent.mainsizer.Hide(4)
            self.Parent.mainsizer.Show(2)
            self.Parent.photopanel.SetFocus()
            self.Parent.mainsizer.Layout()
            self.Parent.photopanel.Layout()
            self.Parent.photopanel.timer.Start(1000)  #Generate a timer event every second                  #starts the timer for the picture on display, calls the ontimer function every sec 
            self.Parent.photopanel.resptime = time.time()                                                 #for recording the response time, it stores the current time when the picture is displayed, and later when a response comes it can be subtracted from time.time() to get the response time                        
            self.Parent.photopanel.timeToLive = 5                                                         #time limit for a particular image, setting it back to 5, as it is being modified in the ontimer funciton 
            self.Parent.photopanel.Bind(wx.EVT_TIMER, self.Parent.photopanel.onTimer, self.Parent.photopanel.timer)                           #binding the timer            
        elif self.nextpanel == 2:
            #showing setpanel (PhotoPanel)
            self.Parent.mainsizer.Hide(4)
            self.Parent.mainsizer.Show(2)
            self.Parent.photopanel.SetFocus()
            self.Parent.mainsizer.Layout()
            self.Parent.photopanel.Layout()
            #setting responses of a particular set null after each set, so that responses of a new set can be appended in an empty set 
            self.Parent.photopanel.responses = []   
            
            #setting timetolive = 5 after each photo change
            self.Parent.photopanel.timeToLive = 5
            #if self.Parent.photopanel.leftBtn.HasFocus() or self.Parent.photopanel.rightBtn.HasFocus():
                #win32api.SetCursorPos(((self.Parent.GetSize()[0] + self.Parent.GetPosition()[0])//2, (self.Parent.GetSize()[1] + self.Parent.GetPosition()[1])//2))
            
            #calls ontimer function ever 1 sec
            self.Parent.photopanel.timer.Start(1000)
            #using time.time() to store the current time to obtain response time, response time can be obtained using this by recording the time at which user responds, and then subtracting it from the the time at the start 
            self.Parent.photopanel.resptime = time.time()
    
if __name__=='__main__' :  
    app=wx.App()
    splash = MySplashScreen()
    splash.Show()    
    app.MainLoop()
    
