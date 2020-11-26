import json
import nltk
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import checkPlantName as c
import timeit

data = '/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/diabetes/54.txt'
with open(data, encoding='utf-8') as f:
    text = f.read()
#


import glob

files = glob.glob('/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/ALL/*.txt')


def read_all(files):
    a = ''

    for j in files:
        try:
            with open(j, encoding='utf-8') as f:
                text = f.read()
        except:
            try:
                with open(j, encoding='utf-16') as f:
                    text = f.read()
            except:
                with open(j, encoding='latin-1') as f:
                    text = f.read()

        a += text

    return a


text = read_all(files)


# ================================ remove stop words ===========================================

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(text)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

filtered_sentence = [i for i in filtered_sentence if not len(i) == 2]

# ============================= remove int ===============================

f = []
for i in filtered_sentence:
    try:
        a = int(i)
    except:
        f.append(i)
# ======================================== remove all caps words ======================
cap = [i for i in f if not i.isupper()]
# ======================================== get only first caps words ======================
cap = [i for i in cap if i[0].isupper()]

# ======================================= find any - alpha numerica=======================

cap = [i for i in cap if i.isalnum()]

# ======================================== remove englihs words =====================
import enchant

d = enchant.Dict("en_US")
cap = [i for i in cap if not d.check(i)]

# ============================= remove if more than two capital letters =======================

sliced = []
for i in cap:
    count = 0
    for j in i:
        if j.isupper():
            count += 1
    if not count < 1:
        sliced.append(i)

cap = sliced
#  ================================ check if it is a plant name ==================
cap = [i for i in cap if c.find_plant(i, '')]
cap = list(set(cap))

# cancer = ['Oroxylum indicum', 'Elephantopus scaber', 'Elephantopus scaber', 'Ailanthus grandis', 'Ailanthus grandis', 'Rubia cordifolia', 'Rubia cordifolia', 'Dillenia species', 'Dillenia (', 'Dillenia species', 'Dillenia species', 'Dillenia species', 'Dillenia species', 'Dillenia undergone', 'Dillenia species', 'Dillenia pentagyna', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Larrea tridentata', 'Premna tomentosa', 'Premna tomentosa', 'Aucklandia costus', 'Aucklandia costus', 'Aucklandia lappa', 'Carica papaya', 'Carica papaya', 'Carica papaya', 'Osyris wightiana', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum tenuiflorum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum basilicum', 'Sanguinaria canadensis', 'Scutia commersonii', 'Viscum album', 'Trigonella foenum-graecum', 'Trigonella foenum-graecum', 'Trigonella foenum', 'Trigonella foenum', 'Trigonella foenum', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus often', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Gynandropsis gynandra', 'Gynandropsis gynandra', 'Gynura cusimbua', 'Hedyotis scandens', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Curcuma longa', 'Saussurea lappa', 'Saussurea costus', 'Saussurea costus', 'Saussurea lappa', 'Podophyllum peltatum', 'Podophyllum hexandrum', 'Allium plants', 'Allium sativum', 'Nyctanthes arbortristis', 'Cinnamomum verum', 'Cinnamomum verum', 'Commiphora mukul', 'Commiphora mukul', 'Catharanthus roseus', 'Hydnocarpus wightiana', 'Hydnocarpus wightiana', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Merremia emerginata', 'Achyranthes aspera', 'Clerodendrum glandulosum', 'Clerodendrum glandulosum', 'Clerodendrum viscosum', 'Clerodendrum viscosum', 'Clerodendrum viscosum', 'Correa influence', 'Correa used', 'Castilleja linariaefolia', 'Castilleja linariaefolia', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Berberis aristata', 'Berberis aristata', 'Flemingia strobilifera', 'Millettia pinnata', 'Euphorbia neriifolia', 'Abrus lectins', 'Abrus lectins', 'Helicteres isora', 'Tabernaemontana heyneana', 'Gossypium schottii', 'Gossypium schottii', 'Potentilla fulgens', 'Blepharis maderaspatensis', 'Ferula assa-foetida', 'Arctium minus', 'Andrographis paniculata', 'Andrographis paniculata', 'Andrographis lineata', 'Andrographis lineata', 'Andrographis paniculata', 'Andrographis paniculata', 'Andrographis paniculata', 'Tecomella undulata', 'Tecomella undulata', 'Tecomella undulata', 'Tecomella undulata', 'Tecomella undulata', 'Maianthemum dilatatum', 'Argemone oil', 'Blumeopsis flava', 'Momordica charantia', 'Benincasa hispida', 'Benincasa hispida', 'Benincasa hispida', 'Hernandia peltata', 'Hernandia nymphaeifolia', 'Hernandia peltata', 'Aphloia theiformis', 'Aphloia theiformis', 'Aphloia theiformis', 'Simaba cuspidata', 'Simaba cuspidata', 'Suaeda maritima', 'Suaeda maritima', 'Geniostoma borbonicum', 'Hyssopus officinalis', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Cynodon dactylon', 'Hygrophila spinosa', 'Vernonia condensata', 'Vernonia genus', 'Vernonia condensata', 'Vernonia condensata', 'Vernonia condensata', 'Psiadia dentata', 'Psiadia arguta', 'Psiadia dentata', 'Paederia foetida', 'Paederia foetida', 'Ophiorrhiza mungos', 'Artemisia nilagirica', 'Artemisia nilagirica', 'Artemisia nilagirica', 'Sarcophyton trochliophorum', 'Sarcophyton glaucum', 'Sarcophyton glaucum', 'Zingiber officinale', 'Saba I', 'Centella asiatica', 'Amaranthus tristis', 'Lavandula bipinnata', 'Nothapodytes foetida', 'Mentha viridis', 'Spermacoce verticillata', 'Caesalpinia bonduc', 'Caesalpinia bonduc', 'Crassocephalum rubens', 'Crassocephalum rubens', 'Crassocephalum rubens', 'Buddleja salviifolia', 'Blumea .', 'Blumea (', 'Blumea lanceolaria', 'Wrightia arborea', 'Wrightia arborea', 'Wrightia arborea', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Arnebia nobilis', 'Mikania cordata', 'Mikania cordata', 'Lantana camara', 'Lysichiton americanus', 'Salacia oblonga', 'Salacia oblonga', 'Salacia oblonga', 'Salacia Oblonga', 'Swertia chirata', 'Swertia chirata', 'Swertia chirata', 'Swertia chirata', 'Dioon spinulosum', 'Dioon spinulosum', 'Anogeissus latifolia', 'Anogeissus latifolia', 'Saponaria officinalis', 'Moringa oleifera', 'Moringa oleiferna', 'Moringa oleiferna', 'Moringa oleifera', 'Moringa oleifera', 'Moringa oleifera', 'Moringa extract', 'Tridax Procumbens', 'Gymnosporia rothiana', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata', 'Origanum vulgare', 'Origanum majorana', 'Terminalia (', 'Terminalia amongst', 'Terminalia species', 'Terminalia chebula', 'Terminalia species', 'Terminalia species', 'Terminalia species', 'Terminalia species', 'Terminalia species', 'Terminalia arjuna', 'Terminalia bellerica', 'Terminalia catappa', 'Terminalia species', 'Terminalia bellerica', 'Terminalia bellerica', 'Terminalia bentzoe', 'Terminalia arjuna', 'Terminalia arjuna', 'Terminalia chebula', 'Terminalia chebula', 'Terminalia chebula', 'Terminalia belerica', 'Glycosmis pentaphylla', 'Glycosmis pentaphylla', 'Glycosmis pentaphylla', 'Glycosmis pentaphylla', 'Glycosmis pentaphylla', 'Hamelia patens', 'Hamelia patens', 'Scoparia dulcis', 'Scoparia dulcis', 'Mucuna pruriens', 'Mucuna pruriens', 'Psidium guajava', 'Psidium guajava', 'Trianthema portulacastrum', 'Trianthema portulacastrum', 'Trianthema portulacastrum', 'Trianthema portulacastrum', 'Calotropis procera', 'Nuxia verticillata', 'Barringtonia racemosa', 'Barringtonia racemosa', 'Azadirachta Indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta Indica', 'Nerium oleander', 'Phyllanthus emblica', 'Phyllanthus emblica', 'Phyllanthus emblica', 'Phyllanthus amarus', 'Phyllanthus amarus', 'Phyllanthus emblica', 'Phyllanthus emblica', 'Streblus asper', 'Semecarpus anacardium', 'Semecarpus anacardium', 'Semecarpus anacardium', 'Taxus baccata', 'Pterospermum acerifolium', 'Pterospermum acerifolium', 'Butea monosperma', 'Butea monosperma', 'Butea monosperma', 'Butea monosperma', 'Butea monosperma', 'Albizia lebbeck', 'Albizia lebbeck', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Soymida fembrifuga', 'Soymida febrifuga', 'Soymida febrifuga', 'Costus speciosus', 'Costus roots', 'Asclepias curassavica', 'Alangium lamarckii', 'Alangium lamarckii', 'Alangium lamarckii', 'Markhamia tomentosa', 'Markhamia tomentosa', 'Markhamia tomentosa', 'Areca alkaloids', 'Areca nut', 'Areca cattechu', 'Areca catechu', 'Areca catechu', 'Areca nut', 'Oplopanax horridus', 'Oplopanax horridus', 'Eupatorium riparium', 'Hiptage benghalensis', 'Acorus calamus', 'Acorus calamus', 'Acorus calamus', 'Pergularia pallida', 'Pergularia pallida']
# fever = ['Elephantopus scaber', 'Elephantopus scaber', 'Mukia madarasepatana', 'Mukia madarasepatana', 'Rhamnus purshianus', 'Rhamnus purshianus', 'Rubus spectabilis', 'Rubus spectabilis', 'Rubus spectabilis', 'Rubus spectabilis', 'Populus tremuloides', 'Populus tremuloides', 'Populus tremuloides', 'Populus tremuloides', 'Rubia cordifolia', 'Tinospora :', 'Tinospora includes', 'Tinospora species', 'Tinospora species', 'Tinospora reveal', 'Tinospora :', 'Tinospora includes', 'Tinospora species', 'Tinospora species', 'Tinospora reveal', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Quercus garryana', 'Quercus garryana', 'Larrea tridentata', 'Premna tomentosa', 'Premna tomentosa', 'Cornus nuttallii', 'Cornus nuttallii', 'Carica papaya', 'Carica papaya', 'Carica papaya', 'Osyris wightiana', 'Osyris wightiana', 'Osyris wightiana', 'Mollugo nudicaulis', 'Mollugo nudicaulis', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Glyptopetalum calocarpum', 'Glyptopetalum calocarpum', 'Glyptopetalum calocarpum', 'Glyptopetalum calocarpum', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa natans', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa natans', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Scutia commersonii', 'Trigonella foenum-graecum', 'Trigonella foenum-graecum', 'Trigonella foenum', 'Trigonella foenum', 'Trigonella foenum', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus often', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus often', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Gynandropsis gynandra', 'Gynandropsis gynandra', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Curcuma longa', 'Bidens pilosa', 'Bidens pilosa', 'Allium plants', 'Cinnamomum verum', 'Cinnamomum verum', 'Catharanthus roseus', 'Catharanthus roseus', 'Catharanthus roseus', 'Hydnocarpus wightiana', 'Hydnocarpus wightiana', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Correa M', 'Correa seed', 'Correa (', 'Correa .', 'Correa seed', 'Correa (', 'Correa .', 'Correa influence', 'Correa used', 'Correa M', 'Clerodendrum viscosum', 'Clerodendrum viscosum', 'Clerodendrum viscosum', 'Erythrina indica', 'Erythrina indica', 'Plumbago zeylanica', 'Plumbago zeylanica.Retrospective', 'Berberis aristata', 'Berberis aristata', 'Berberis aristata', 'Berberis aristata', 'Berberis aristata', 'Berberis aristata', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Pedicularis plants', 'Pedicularis plants', 'Pedicularis plants', 'Pedicularis plants', 'Pedicularis genus', 'Pedicularis longiflora', 'Pedicularis .', 'Pedicularis .', 'Pedicularis explore', 'Pedicularis plants', 'Pedicularis plants', 'Pedicularis plants', 'Pedicularis plants', 'Pedicularis genus', 'Pedicularis longiflora', 'Pedicularis .', 'Pedicularis .', 'Pedicularis explore', 'Euphorbia nivulia', 'Euphorbia nivulia', 'Euphorbia nivulia', 'Euphorbia nivulia', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Helicteres isora', 'Shorea robusta', 'Shorea robusta', 'Shorea robusta', 'Shorea robusta', 'Mahonia spp.', 'Mahonia spp.', 'Pongamia pinnata', 'Pongamia pinnata', 'Momordica charantia', 'Thespesia populnea', 'Thespesia populnea', 'Thespesia populnea', 'Thespesia populnea', 'Thespesia populnea', 'Thespesia populnea', 'Thespesia populnea', 'Thespesia populnea', 'Aphloia theiformis', 'Suaeda maritima', 'Suaeda maritima', 'Geniostoma borbonicum', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Alnus rubra', 'Alnus rubra', 'Aspidosperma spp', 'Aspidosperma spp', 'Pseudotsuga menziesii', 'Pseudotsuga menziesii', 'Pseudotsuga menziesii', 'Pseudotsuga menziesii', 'Pseudotsuga menziesii', 'Pseudotsuga menziesii', 'Psiadia dentata', 'Psiadia arguta', 'Psiadia dentata', 'Sida acuta', 'Sida rhombifolia', 'Sida acuta', 'Sida rhombifolia', 'Symphoricarpos albus', 'Symphoricarpos albus', 'Sarcophyton trochliophorum', 'Sarcophyton glaucum', 'Sarcophyton glaucum', 'Zingiber officinale', 'Abies grandis', 'Abies grandis', 'Abies grandis', 'Abies grandis', 'Abies grandis', 'Abies grandis', 'Lavandula bipinnata', 'Abutilon indicum', 'Abutilon indicum', 'Abutilon indicum', 'Abutilon indicum', 'Sambucus racemosa', 'Sambucus racemosa', 'Fagonia cretica', 'Fagonia cretica', 'Buddleja salviifolia', 'Wrightia arborea', 'Wrightia arborea', 'Wrightia arborea', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Indigofera asphalathoides', 'Indigofera asphalathoides', 'Swertia chirata', 'Swertia chirata', 'Swertia chirata', 'Swertia chirata', 'Hybanthus enneaspermus', 'Hybanthus enneaspermus', 'Anogeissus latifolia', 'Anogeissus latifolia', 'Saponaria officinalis', 'Saponaria officinalis', 'Saponaria officinalis', 'Moringa oleiferna', 'Moringa oleiferna', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata', 'Terminalia chebula', 'Terminalia belerica', 'Terminalia bentzoe', 'Terminalia bellerica', 'Terminalia bellerica', 'Glycosmis pentaphylla', 'Glycosmis pentaphylla', 'Glycosmis pentaphylla', 'Glycosmis pentaphylla', 'Glycosmis pentaphylla', 'Mucuna pruriens', 'Mucuna pruriens', 'Psidium guajava', 'Psidium guajava', 'Psidium guajava', 'Psidium guajava', 'Trianthema portulacastrum', 'Trianthema portulacastrum', 'Nuxia verticillata', 'Barringtonia racemosa', 'Barringtonia racemosa', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta Indica', 'Azadirachta Indica', 'Azadirachta Indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Prunus emarginata', 'Prunus emarginata', 'Prunus emarginata', 'Prunus emarginata', 'Nerium oleander', 'Ampelozizyphus amazonicus', 'Ampelozizyphus amazonicus', 'Ampelozizyphus amazonicus', 'Ampelozizyphus amazonicus', 'Phyllanthus emblica', 'Phyllanthus emblica', 'Phyllanthus emblica', 'Phyllanthus amarus', 'Phyllanthus amarus', 'Phyllanthus emblica', 'Phyllanthus emblica', 'Cardiospermum halicacabum', 'Cardiospermum halicacabum', 'Cardiospermum halicacabum', 'Cardiospermum halicacabum', 'Streblus asper', 'Streblus asper', 'Streblus asper', 'Semecarpus anacardium', 'Casearia elliptica', 'Casearia elliptica', 'Malus fusca', 'Malus fusca', 'Pterospermum acerifolium', 'Pterospermum acerifolium', 'Butea monosperma', 'Butea monosperma', 'Butea monosperma', 'Butea monosperma', 'Butea monosperma', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Soymida febrifuga', 'Soymida febrifuga', 'Soymida fembrifuga', 'Tagetes neisonii', 'Tagetes neisonii', 'Holarrhena pubescens', 'Holarrhena pubescens', 'Markhamia tomentosa', 'Markhamia tomentosa', 'Markhamia tomentosa', 'Alangium lamarckii', 'Alangium lamarckii', 'Oplopanax horridus', 'Oplopanax horridus', 'Oplopanax horridus', 'Oplopanax horridus', 'Oplopanax horridus', 'Oplopanax horridus', 'Eupatorium riparium', 'Hiptage benghalensis', 'Acorus calamus', 'Acorus calamus', 'Acorus calamus', 'Acorus calamus', 'Acorus calamus', 'Acorus calamus', 'Acorus calamus', 'Pergularia pallida']
# arthidis = ['Garcinia mangostana', 'Oplopanax horridus', 'Oplopanax horridus', 'Gymnema sylvestre', 'Correa seed', 'Correa (', 'Acorus calamus', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Argyreia speciosa', 'Celastrus species', 'Celastrus (', 'Celastrus species', 'Celastrus species', 'Celastrus genus', 'Celastrus confirmed', 'Celastrus paniculatus', 'Celastrus orbiculatus', 'Celastrus .', 'Celastrus species', 'Celastrus (', 'Celastrus species', 'Celastrus species', 'Celastrus genus', 'Celastrus confirmed', 'Celastrus paniculatus', 'Celastrus orbiculatus', 'Celastrus .', 'Withania somnifera', 'Thespesia populnea', 'Thespesia populnea', 'Thespesia populnea', 'Thespesia populnea', 'Commiphora mukul.A', 'Saussurea lappa', 'Vanda roxburghii', 'Cyperus scariosus', 'Achyranthes aspera', 'Curcuma longa', 'Curcuma longa', 'Vigna mungo', 'Vigna mungo', 'Benincasa hispida', 'Benincasa hispida', 'Benincasa hispida', 'Tinospora :', 'Tinospora includes', 'Tinospora species', 'Tinospora species', 'Tinospora reveal', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Semecarpus anacardium', 'Semecarpus anacardium', 'Semecarpus anacardium', 'Semecarpus anacardium', 'Semecarpus anacardium', 'Semecarpus anacardium', 'Semecarpus anacardium']
# diabetes= ['Hedyotis scandens', 'Sarcostemma brevistigma', 'Sarcostemma brevistigma', 'Sarcostemma brevistigma', 'Correa .', 'Correa Roxb', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Acorus calamus', 'Abies balsamea', 'Abies balsamea', 'Abies grandis', 'Abies grandis', 'Abies grandis', 'Pinus banksiana', 'Vaccinium vitis-idaea', 'Diospyros melanoxylon', 'Diospyros melanoxylon', 'Diospyros melanoxylon', 'Oroxylum indicum', 'Oroxylum indicum', 'Oroxylum indicum', 'Alnus incana', 'Alnus rubra', 'Curcuma domestica', 'Curcuma longa', 'Curcuma longa', 'Curcuma longa', 'Curcuma longa', 'Curcuma longa', 'Curcuma longa', 'Curcuma longa', 'Curcuma longa', 'Curcuma longa', 'Cyperus scariosus', 'Cyperus rotundus', 'Cyperus scariosus', 'Cyperus rotundus', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Populus tremuloides', 'Populus tremuloides', 'Brassica campestris', 'Brassica campestris', 'Brassica juncea', 'Brassica juncea', 'Brassica juncea', 'Litsea :', 'Litsea one', 'Litsea species', 'Litsea species', 'Litsea species', 'Litsea species', 'Litsea Species', 'Litsea show', 'Litsea comprises', 'Litsea species', 'Litsea pharmacological', 'Litsea species', 'Symphoricarpos albus', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta Indica', 'Picea mariana', 'Picea glauca', 'Kalmia angustifolia', 'Solanum americanum', 'Casearia esculenta', 'Eclipta prostrata', 'Cajanus cajan', 'Morus indica', 'Morus alba', 'Morus alba', 'Morus alba', 'Justicia secunda', 'Osyris wightiana', 'Lagerstroemia speciosa', 'Sarracenia purpurea', 'Sambucus racemosa', 'Tanacetum nubigenum', 'Tanacetum nubigenum', 'Tanacetum nubigenum', 'Tanacetum nubigenum', 'Pterocarpus marsupium', 'Pterocarpus marsupium', 'Pterocarpus santalinus', 'Pterocarpus santalinus', 'Pterocarpus marsupium', 'Pterocarpus marsupium', 'Pterocarpus marsupium', 'Pterocarpus marsupium', 'Pterocarpus marsupium', 'Pterocarpus marsupium', 'Pterocarpus marsupium', 'Pterocarpus marsupium', 'Anacyclus pyrethrum', 'Solidago canadensis', 'Lycopodium clavatum', 'Paederia foetida', 'Paederia foetida', 'Cicer arietum', 'Artemisia pallens', 'Artemisia pallens', 'Jatropha curcus', 'Jatropha curcus', 'Cucumis sativus', 'Cucumis melo', 'Cucumis melo', 'Cucumis prophetarum', 'Cucumis prophetarum', 'Areca catechu', 'Benincasa hispida', 'Benincasa hispida', 'Benincasa hispida', 'Benincasa hispida', 'Benincasa hispida', 'Benincasa hispida', 'Nerium oleander', 'Trichosanthes cucumerina', 'Trichosanthes dioica', 'Hydnocarpus wightiana', 'Hydnocarpus wightiana', 'Quercus garryana', 'Quercus alba', 'Ayapana triplinervis', 'Beyeria leshnaultii', 'Mahonia spp.', 'Ocimum sanctum', 'Ocimum tenuiflorum', 'Ocimum gratissimum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum tenuiflorum', 'Ocimum tenuiflorum', 'Ocimum tenuiflorum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum.Exploration', 'Ocimum sanctum', 'Ocimum sanctum', 'Andrographis paniculata', 'Andrographis paniculata', 'Andrographis paniculata', 'Andrographis paniculata', 'Andrographis paniculata', 'Zingiber officinale', 'Zingiber officinale', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cardifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora includes', 'Tinospora species', 'Tinospora species', 'Tinospora reveal', 'Tinospora cordifolia', 'Symplocos cochinchinensis', 'Melia azedarach', 'Melia azedarach', 'Melia azaderach', 'Stevia rebaudiana', 'Stevia rebaudiana', 'Tragia involucrata', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Musa paradisiaca', 'Musa paradisiaca', 'Musa AAA', 'Musa AAA', 'Musa AAA', 'Musa AAA', 'Bixa orellana', 'Bixa orellana', 'Bixa orellana', 'Biophytum sensitivum', 'Biophytum sensitivum', 'Pseudotsuga menziesii', 'Pseudotsuga menziesii', 'Pseudotsuga menziesii', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Phyllanthus emblica', 'Phyllanthus emblica', 'Phyllanthus emblica', 'Phyllanthus emblica', 'Phyllanthus amarus', 'Phyllanthus amarus', 'Phyllanthus amarus', 'Phyllanthus niruri', 'Rubus spectabilis', 'Rubus spectabilis', 'Abutilon indicum', 'Triticum aestivum', 'Petroselinum crispum', 'Mangifera indica', 'Gynura cusimbua', 'Swertia chirayita', 'Swertia chirayita', 'Swertia cordata', 'Swertia chirayita', 'Swertia cordata', 'Swertia chirayita', 'Swertia cordata', 'Swertia chirayita', 'Swertia species', 'Swertia contain', 'Swertia chirayita', 'Swertia cordata', 'Swertia chirayita', 'Cinnamomum tamala', 'Cinnamomum verum', 'Swietenia mahagoni', 'Swietenia mahagoni', 'Mucuna prurita', 'Mucuna pruriens', 'Mucuna pruriens', 'Mucuna pruriens', 'Mucuna pruriens', 'Caesalpinia bonducella', 'Malus fusca', 'Costus igneus', 'Costus speciosus', 'Costus speciosus', 'Dendrocalamus hamiltonii', 'Zanthoxylum alatum', 'Zanthoxylum alatum', 'Zanthoxylum alatum', 'Gaultheria hispidula', 'Salacia reticulata', 'Salacia (', 'Salacia oblonga', 'Salacia oblonga', 'Coptis chinensis', 'Moringa oleifera', 'Moringa oleifera', 'Moringa oleifera', 'Moringa oleifera', 'Moringa pterygosperma', 'Moringa oleifera', 'Moringa oleifera', 'Oplopanax horridus', 'Oplopanax horridus', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelose', 'Aegle marmelos', 'Aegle marmelos', 'Allium sativum', 'Allium sativum', 'Allium sativum', 'Allium sativum', 'Allium carolinianum', 'Allium sativum', 'Allium sativum', 'Allium sativum', 'Allium sativum', 'Allium sativum', 'Allium cepa', 'Allium sativum', 'Rhamnus purshianus', 'Cyclea peltata', 'Bambusa dendrocalamus', 'Blumeopsis flava', 'Larix laricina', 'Larix laricina', 'Larix laricina', 'Larix laricina', 'Larix laricina', 'Saba ,', 'Murraya koenigii', 'Murraya koenigii', 'Murraya koeingii', 'Rhus hirta', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Psidium guajava', 'Mentha piperitae', 'Phaseolus mungo', 'Phaseolus mungo', 'Phaseolus mungo', 'Phaseolus aureus', 'Linum usitatisumum', 'Linum usitatisumum', 'Linum usitatisumum', 'Clerodendrum glandulosum', 'Clerodendrum glandulosum', 'Centella asiatica', 'Centella asiatica', 'Centella asiatica', 'Boerhavia diffusa', 'Boerhavia diffusa', 'Trigonella foenum', 'Trigonella foenum', 'Trigonella foenum', 'Trigonella seed', 'Trigonella seed', 'Trigonella foenum', 'Trigonella foenum', 'Trigonella foenum', 'Trigonella foenum', 'Trigonella foenum', 'Trigonella foenum-graceum', 'Trigonella foenum', 'Trigonella foenum', 'Trigonella seed', 'Trigonella seed', 'Trigonella seed', 'Trigonella seed', 'Adansonia digitata', 'Rauvolfia serpentina', 'Streblus asper', 'Streblus asper', 'Cornus nuttallii', 'Cornus stolonifera', 'Vinca rosea', 'Vinca rosea', 'Vinca rosea', 'Blumea aromatica', 'Blumea aromatica', 'Blumea species', 'Terminalia arjuna', 'Terminalia chebula', 'Terminalia belerica', 'Terminalia bellirica', 'Terminalia chebula', 'Terminalia bellirica', 'Terminalia amongst', 'Terminalia species', 'Terminalia chebula', 'Terminalia species', 'Terminalia species', 'Terminalia species', 'Terminalia species', 'Terminalia species', 'Terminalia arjuna', 'Terminalia bellerica', 'Terminalia catappa', 'Terminalia species', 'Terminalia bellerica', 'Terminalia bellerica', 'Terminalia chebula', 'Santalum spicatum', 'Syzygium cumin', 'Syzygium jambolanum', 'Syzygium jambolanum', 'Syzygium cumini', 'Syzygium cumini', 'Syzygium cumini', 'Syzygium cumini', 'Syzygium cumini', 'Euphorbia nivulia', 'Euphorbia drummondii', 'Euphorbia drummondii', 'Premna integrifolia', 'Schisandra grandiflora', 'Schisandra grandiflora', 'Glycyrrhiza glabra', 'Prunus emarginata', 'Prunus emarginata', 'Catharanthus roseus', 'Catharanthus roseus', 'Catharanthus roseus', 'Boswellia serrata', 'Saponaria officinalis', 'Coccinia indica', 'Coccinia indica', 'Coccinia indica', 'Coccinia grandis', 'Coccinia indica', 'Berberis aristata']
# plants_dict_arthids = [('Semecarpus anacardium', 7), ('Ocimum sanctum', 6), ('Celastrus species', 6), ('Tinospora cordifolia', 5), ('Thespesia populnea', 4), ('Benincasa hispida', 3), ('Oplopanax horridus', 2), ('Celastrus genus', 2), ('Celastrus confirmed', 2), ('Celastrus paniculatus', 2), ('Celastrus orbiculatus', 2), ('Curcuma longa', 2), ('Vigna mungo', 2), ('Tinospora species', 2), ('Garcinia mangostana', 1), ('Gymnema sylvestre', 1), ('Correa seed', 1)]


plant_list = []
for i in cap:
    match_list = [k for k, e in enumerate(filtered_sentence) if e == i]
    for j in match_list:
        plant_list.append(filtered_sentence[j] + ' ' + filtered_sentence[j + 1])

print(len(plant_list))

plants_dict = {}
for i in plant_list:
    if i in plants_dict:
        plants_dict[i] += 1
    else:
        plants_dict.update({i: 1})

plants_dict = sorted(plants_dict.keys(), key=lambda x: x[1], reverse=True)[:20]

x = [i[0] for i in plants_dict]
y = [i[1] for i in plants_dict]
#
# # ============================ abstracts sepration based on disaes =================
#
# from matplotlib import pyplot as plt
# plt.barh(x,y)
# plt.title('Top 20 Rank Plants on Arthritis')
# plt.ylabel('Plant Name')
# plt.xlabel('Number of Occurrence')
# # plt.yticks(rotation=90)
# plt.show()
# #


# =========================================
cancer = ['Oroxylum indicum', 'Elephantopus scaber', 'Elephantopus scaber', 'Ailanthus grandis', 'Ailanthus grandis',
          'Rubia cordifolia', 'Rubia cordifolia', 'Dillenia species', 'Dillenia (', 'Dillenia species',
          'Dillenia species', 'Dillenia species', 'Dillenia species', 'Dillenia undergone', 'Dillenia species',
          'Dillenia pentagyna', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia',
          'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Larrea tridentata',
          'Premna tomentosa', 'Premna tomentosa', 'Aucklandia costus', 'Aucklandia costus', 'Aucklandia lappa',
          'Carica papaya', 'Carica papaya', 'Carica papaya', 'Osyris wightiana', 'Ocimum sanctum', 'Ocimum sanctum',
          'Ocimum tenuiflorum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum',
          'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum basilicum', 'Sanguinaria canadensis', 'Scutia commersonii',
          'Viscum album', 'Trigonella foenum-graecum', 'Trigonella foenum-graecum', 'Trigonella foenum',
          'Trigonella foenum', 'Trigonella foenum', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus often',
          'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus',
          'Gynandropsis gynandra', 'Gynandropsis gynandra', 'Gynura cusimbua', 'Hedyotis scandens',
          'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum',
          'Heliotropium indicum', 'Curcuma longa', 'Saussurea lappa', 'Saussurea costus', 'Saussurea costus',
          'Saussurea lappa', 'Podophyllum peltatum', 'Podophyllum hexandrum', 'Allium plants', 'Allium sativum',
          'Nyctanthes arbortristis', 'Cinnamomum verum', 'Cinnamomum verum', 'Commiphora mukul', 'Commiphora mukul',
          'Catharanthus roseus', 'Hydnocarpus wightiana', 'Hydnocarpus wightiana', 'Withania somnifera',
          'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera',
          'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera',
          'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera',
          'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera',
          'Withania somnifera', 'Merremia emerginata', 'Achyranthes aspera', 'Clerodendrum glandulosum',
          'Clerodendrum glandulosum', 'Clerodendrum viscosum', 'Clerodendrum viscosum', 'Clerodendrum viscosum',
          'Correa influence', 'Correa used', 'Castilleja linariaefolia', 'Castilleja linariaefolia',
          'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda',
          'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda',
          'Berberis aristata', 'Berberis aristata', 'Flemingia strobilifera', 'Millettia pinnata',
          'Euphorbia neriifolia', 'Abrus lectins', 'Abrus lectins', 'Helicteres isora', 'Tabernaemontana heyneana',
          'Gossypium schottii', 'Gossypium schottii', 'Potentilla fulgens', 'Blepharis maderaspatensis',
          'Ferula assa-foetida', 'Arctium minus', 'Andrographis paniculata', 'Andrographis paniculata',
          'Andrographis lineata', 'Andrographis lineata', 'Andrographis paniculata', 'Andrographis paniculata',
          'Andrographis paniculata', 'Tecomella undulata', 'Tecomella undulata', 'Tecomella undulata',
          'Tecomella undulata', 'Tecomella undulata', 'Maianthemum dilatatum', 'Argemone oil', 'Blumeopsis flava',
          'Momordica charantia', 'Benincasa hispida', 'Benincasa hispida', 'Benincasa hispida', 'Hernandia peltata',
          'Hernandia nymphaeifolia', 'Hernandia peltata', 'Aphloia theiformis', 'Aphloia theiformis',
          'Aphloia theiformis', 'Simaba cuspidata', 'Simaba cuspidata', 'Suaeda maritima', 'Suaeda maritima',
          'Geniostoma borbonicum', 'Hyssopus officinalis', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos',
          'Aegle marmelos', 'Aegle marmelos', 'Cynodon dactylon', 'Hygrophila spinosa', 'Vernonia condensata',
          'Vernonia genus', 'Vernonia condensata', 'Vernonia condensata', 'Vernonia condensata', 'Psiadia dentata',
          'Psiadia arguta', 'Psiadia dentata', 'Paederia foetida', 'Paederia foetida', 'Ophiorrhiza mungos',
          'Artemisia nilagirica', 'Artemisia nilagirica', 'Artemisia nilagirica', 'Sarcophyton trochliophorum',
          'Sarcophyton glaucum', 'Sarcophyton glaucum', 'Zingiber officinale', 'Saba I', 'Centella asiatica',
          'Amaranthus tristis', 'Lavandula bipinnata', 'Nothapodytes foetida', 'Mentha viridis',
          'Spermacoce verticillata', 'Caesalpinia bonduc', 'Caesalpinia bonduc', 'Crassocephalum rubens',
          'Crassocephalum rubens', 'Crassocephalum rubens', 'Buddleja salviifolia', 'Blumea .', 'Blumea (',
          'Blumea lanceolaria', 'Wrightia arborea', 'Wrightia arborea', 'Wrightia arborea', 'Selaginella bryopteris',
          'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris',
          'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Arnebia nobilis',
          'Mikania cordata', 'Mikania cordata', 'Lantana camara', 'Lysichiton americanus', 'Salacia oblonga',
          'Salacia oblonga', 'Salacia oblonga', 'Salacia Oblonga', 'Swertia chirata', 'Swertia chirata',
          'Swertia chirata', 'Swertia chirata', 'Dioon spinulosum', 'Dioon spinulosum', 'Anogeissus latifolia',
          'Anogeissus latifolia', 'Saponaria officinalis', 'Moringa oleifera', 'Moringa oleiferna', 'Moringa oleiferna',
          'Moringa oleifera', 'Moringa oleifera', 'Moringa oleifera', 'Moringa extract', 'Tridax Procumbens',
          'Gymnosporia rothiana', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata',
          'Origanum vulgare', 'Origanum majorana', 'Terminalia (', 'Terminalia amongst', 'Terminalia species',
          'Terminalia chebula', 'Terminalia species', 'Terminalia species', 'Terminalia species', 'Terminalia species',
          'Terminalia species', 'Terminalia arjuna', 'Terminalia bellerica', 'Terminalia catappa', 'Terminalia species',
          'Terminalia bellerica', 'Terminalia bellerica', 'Terminalia bentzoe', 'Terminalia arjuna',
          'Terminalia arjuna', 'Terminalia chebula', 'Terminalia chebula', 'Terminalia chebula', 'Terminalia belerica',
          'Glycosmis pentaphylla', 'Glycosmis pentaphylla', 'Glycosmis pentaphylla', 'Glycosmis pentaphylla',
          'Glycosmis pentaphylla', 'Hamelia patens', 'Hamelia patens', 'Scoparia dulcis', 'Scoparia dulcis',
          'Mucuna pruriens', 'Mucuna pruriens', 'Psidium guajava', 'Psidium guajava', 'Trianthema portulacastrum',
          'Trianthema portulacastrum', 'Trianthema portulacastrum', 'Trianthema portulacastrum', 'Calotropis procera',
          'Nuxia verticillata', 'Barringtonia racemosa', 'Barringtonia racemosa', 'Azadirachta Indica',
          'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta Indica', 'Nerium oleander',
          'Phyllanthus emblica', 'Phyllanthus emblica', 'Phyllanthus emblica', 'Phyllanthus amarus',
          'Phyllanthus amarus', 'Phyllanthus emblica', 'Phyllanthus emblica', 'Streblus asper', 'Semecarpus anacardium',
          'Semecarpus anacardium', 'Semecarpus anacardium', 'Taxus baccata', 'Pterospermum acerifolium',
          'Pterospermum acerifolium', 'Butea monosperma', 'Butea monosperma', 'Butea monosperma', 'Butea monosperma',
          'Butea monosperma', 'Albizia lebbeck', 'Albizia lebbeck', 'Neolamarckia cadamba', 'Neolamarckia cadamba',
          'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Soymida fembrifuga', 'Soymida febrifuga',
          'Soymida febrifuga', 'Costus speciosus', 'Costus roots', 'Asclepias curassavica', 'Alangium lamarckii',
          'Alangium lamarckii', 'Alangium lamarckii', 'Markhamia tomentosa', 'Markhamia tomentosa',
          'Markhamia tomentosa', 'Areca alkaloids', 'Areca nut', 'Areca cattechu', 'Areca catechu', 'Areca catechu',
          'Areca nut', 'Oplopanax horridus', 'Oplopanax horridus', 'Eupatorium riparium', 'Hiptage benghalensis',
          'Acorus calamus', 'Acorus calamus', 'Acorus calamus', 'Pergularia pallida', 'Pergularia pallida']
fever = ['Elephantopus scaber', 'Elephantopus scaber', 'Mukia madarasepatana', 'Mukia madarasepatana',
         'Rhamnus purshianus', 'Rhamnus purshianus', 'Rubus spectabilis', 'Rubus spectabilis', 'Rubus spectabilis',
         'Rubus spectabilis', 'Populus tremuloides', 'Populus tremuloides', 'Populus tremuloides',
         'Populus tremuloides', 'Rubia cordifolia', 'Tinospora :', 'Tinospora includes', 'Tinospora species',
         'Tinospora species', 'Tinospora reveal', 'Tinospora :', 'Tinospora includes', 'Tinospora species',
         'Tinospora species', 'Tinospora reveal', 'Tinospora cordifolia', 'Tinospora cordifolia',
         'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia',
         'Quercus garryana', 'Quercus garryana', 'Larrea tridentata', 'Premna tomentosa', 'Premna tomentosa',
         'Cornus nuttallii', 'Cornus nuttallii', 'Carica papaya', 'Carica papaya', 'Carica papaya', 'Osyris wightiana',
         'Osyris wightiana', 'Osyris wightiana', 'Mollugo nudicaulis', 'Mollugo nudicaulis', 'Ocimum sanctum',
         'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum',
         'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum',
         'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum',
         'Ocimum sanctum', 'Ocimum sanctum', 'Glyptopetalum calocarpum', 'Glyptopetalum calocarpum',
         'Glyptopetalum calocarpum', 'Glyptopetalum calocarpum', 'Trapa bispinosa', 'Trapa bispinosa',
         'Trapa bispinosa', 'Trapa natans', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa',
         'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa natans', 'Trapa bispinosa',
         'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Trapa bispinosa', 'Scutia commersonii',
         'Trigonella foenum-graecum', 'Trigonella foenum-graecum', 'Trigonella foenum', 'Trigonella foenum',
         'Trigonella foenum', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus often', 'Hemidesmus indicus',
         'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus',
         'Hemidesmus often', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Hemidesmus indicus',
         'Hemidesmus indicus', 'Gynandropsis gynandra', 'Gynandropsis gynandra', 'Heliotropium indicum',
         'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum',
         'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum',
         'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum', 'Heliotropium indicum',
         'Heliotropium indicum', 'Heliotropium indicum', 'Curcuma longa', 'Bidens pilosa', 'Bidens pilosa',
         'Allium plants', 'Cinnamomum verum', 'Cinnamomum verum', 'Catharanthus roseus', 'Catharanthus roseus',
         'Catharanthus roseus', 'Hydnocarpus wightiana', 'Hydnocarpus wightiana', 'Withania somnifera',
         'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera',
         'Withania somnifera', 'Withania somnifera', 'Correa M', 'Correa seed', 'Correa (', 'Correa .', 'Correa seed',
         'Correa (', 'Correa .', 'Correa influence', 'Correa used', 'Correa M', 'Clerodendrum viscosum',
         'Clerodendrum viscosum', 'Clerodendrum viscosum', 'Erythrina indica', 'Erythrina indica', 'Plumbago zeylanica',
         'Plumbago zeylanica.Retrospective', 'Berberis aristata', 'Berberis aristata', 'Berberis aristata',
         'Berberis aristata', 'Berberis aristata', 'Berberis aristata', 'Stephania rotunda', 'Stephania rotunda',
         'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda',
         'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda',
         'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda',
         'Stephania rotunda', 'Stephania rotunda', 'Stephania rotunda', 'Pedicularis plants', 'Pedicularis plants',
         'Pedicularis plants', 'Pedicularis plants', 'Pedicularis genus', 'Pedicularis longiflora', 'Pedicularis .',
         'Pedicularis .', 'Pedicularis explore', 'Pedicularis plants', 'Pedicularis plants', 'Pedicularis plants',
         'Pedicularis plants', 'Pedicularis genus', 'Pedicularis longiflora', 'Pedicularis .', 'Pedicularis .',
         'Pedicularis explore', 'Euphorbia nivulia', 'Euphorbia nivulia', 'Euphorbia nivulia', 'Euphorbia nivulia',
         'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata',
         'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata', 'Pluchea lanceolata',
         'Pluchea lanceolata', 'Pluchea lanceolata', 'Helicteres isora', 'Shorea robusta', 'Shorea robusta',
         'Shorea robusta', 'Shorea robusta', 'Mahonia spp.', 'Mahonia spp.', 'Pongamia pinnata', 'Pongamia pinnata',
         'Momordica charantia', 'Thespesia populnea', 'Thespesia populnea', 'Thespesia populnea', 'Thespesia populnea',
         'Thespesia populnea', 'Thespesia populnea', 'Thespesia populnea', 'Thespesia populnea', 'Aphloia theiformis',
         'Suaeda maritima', 'Suaeda maritima', 'Geniostoma borbonicum', 'Aegle marmelos', 'Aegle marmelos',
         'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos',
         'Aegle marmelos', 'Aegle marmelos', 'Alnus rubra', 'Alnus rubra', 'Aspidosperma spp', 'Aspidosperma spp',
         'Pseudotsuga menziesii', 'Pseudotsuga menziesii', 'Pseudotsuga menziesii', 'Pseudotsuga menziesii',
         'Pseudotsuga menziesii', 'Pseudotsuga menziesii', 'Psiadia dentata', 'Psiadia arguta', 'Psiadia dentata',
         'Sida acuta', 'Sida rhombifolia', 'Sida acuta', 'Sida rhombifolia', 'Symphoricarpos albus',
         'Symphoricarpos albus', 'Sarcophyton trochliophorum', 'Sarcophyton glaucum', 'Sarcophyton glaucum',
         'Zingiber officinale', 'Abies grandis', 'Abies grandis', 'Abies grandis', 'Abies grandis', 'Abies grandis',
         'Abies grandis', 'Lavandula bipinnata', 'Abutilon indicum', 'Abutilon indicum', 'Abutilon indicum',
         'Abutilon indicum', 'Sambucus racemosa', 'Sambucus racemosa', 'Fagonia cretica', 'Fagonia cretica',
         'Buddleja salviifolia', 'Wrightia arborea', 'Wrightia arborea', 'Wrightia arborea', 'Selaginella bryopteris',
         'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris',
         'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris',
         'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris',
         'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris',
         'Selaginella bryopteris', 'Selaginella bryopteris', 'Selaginella bryopteris', 'Indigofera asphalathoides',
         'Indigofera asphalathoides', 'Swertia chirata', 'Swertia chirata', 'Swertia chirata', 'Swertia chirata',
         'Hybanthus enneaspermus', 'Hybanthus enneaspermus', 'Anogeissus latifolia', 'Anogeissus latifolia',
         'Saponaria officinalis', 'Saponaria officinalis', 'Saponaria officinalis', 'Moringa oleiferna',
         'Moringa oleiferna', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata', 'Aerva lanata',
         'Aerva lanata', 'Aerva lanata', 'Terminalia chebula', 'Terminalia belerica', 'Terminalia bentzoe',
         'Terminalia bellerica', 'Terminalia bellerica', 'Glycosmis pentaphylla', 'Glycosmis pentaphylla',
         'Glycosmis pentaphylla', 'Glycosmis pentaphylla', 'Glycosmis pentaphylla', 'Mucuna pruriens',
         'Mucuna pruriens', 'Psidium guajava', 'Psidium guajava', 'Psidium guajava', 'Psidium guajava',
         'Trianthema portulacastrum', 'Trianthema portulacastrum', 'Nuxia verticillata', 'Barringtonia racemosa',
         'Barringtonia racemosa', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta Indica',
         'Azadirachta Indica', 'Azadirachta Indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica',
         'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Prunus emarginata', 'Prunus emarginata',
         'Prunus emarginata', 'Prunus emarginata', 'Nerium oleander', 'Ampelozizyphus amazonicus',
         'Ampelozizyphus amazonicus', 'Ampelozizyphus amazonicus', 'Ampelozizyphus amazonicus', 'Phyllanthus emblica',
         'Phyllanthus emblica', 'Phyllanthus emblica', 'Phyllanthus amarus', 'Phyllanthus amarus',
         'Phyllanthus emblica', 'Phyllanthus emblica', 'Cardiospermum halicacabum', 'Cardiospermum halicacabum',
         'Cardiospermum halicacabum', 'Cardiospermum halicacabum', 'Streblus asper', 'Streblus asper', 'Streblus asper',
         'Semecarpus anacardium', 'Casearia elliptica', 'Casearia elliptica', 'Malus fusca', 'Malus fusca',
         'Pterospermum acerifolium', 'Pterospermum acerifolium', 'Butea monosperma', 'Butea monosperma',
         'Butea monosperma', 'Butea monosperma', 'Butea monosperma', 'Neolamarckia cadamba', 'Neolamarckia cadamba',
         'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba',
         'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba',
         'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Soymida febrifuga', 'Soymida febrifuga', 'Soymida fembrifuga',
         'Tagetes neisonii', 'Tagetes neisonii', 'Holarrhena pubescens', 'Holarrhena pubescens', 'Markhamia tomentosa',
         'Markhamia tomentosa', 'Markhamia tomentosa', 'Alangium lamarckii', 'Alangium lamarckii', 'Oplopanax horridus',
         'Oplopanax horridus', 'Oplopanax horridus', 'Oplopanax horridus', 'Oplopanax horridus', 'Oplopanax horridus',
         'Eupatorium riparium', 'Hiptage benghalensis', 'Acorus calamus', 'Acorus calamus', 'Acorus calamus',
         'Acorus calamus', 'Acorus calamus', 'Acorus calamus', 'Acorus calamus', 'Pergularia pallida']
arthidis = ['Garcinia mangostana', 'Oplopanax horridus', 'Oplopanax horridus', 'Gymnema sylvestre', 'Correa seed',
            'Correa (', 'Acorus calamus', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum',
            'Ocimum sanctum', 'Ocimum sanctum', 'Argyreia speciosa', 'Celastrus species', 'Celastrus (',
            'Celastrus species', 'Celastrus species', 'Celastrus genus', 'Celastrus confirmed', 'Celastrus paniculatus',
            'Celastrus orbiculatus', 'Celastrus .', 'Celastrus species', 'Celastrus (', 'Celastrus species',
            'Celastrus species', 'Celastrus genus', 'Celastrus confirmed', 'Celastrus paniculatus',
            'Celastrus orbiculatus', 'Celastrus .', 'Withania somnifera', 'Thespesia populnea', 'Thespesia populnea',
            'Thespesia populnea', 'Thespesia populnea', 'Commiphora mukul.A', 'Saussurea lappa', 'Vanda roxburghii',
            'Cyperus scariosus', 'Achyranthes aspera', 'Curcuma longa', 'Curcuma longa', 'Vigna mungo', 'Vigna mungo',
            'Benincasa hispida', 'Benincasa hispida', 'Benincasa hispida', 'Tinospora :', 'Tinospora includes',
            'Tinospora species', 'Tinospora species', 'Tinospora reveal', 'Tinospora cordifolia',
            'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia',
            'Semecarpus anacardium', 'Semecarpus anacardium', 'Semecarpus anacardium', 'Semecarpus anacardium',
            'Semecarpus anacardium', 'Semecarpus anacardium', 'Semecarpus anacardium']
diabetes = ['Hedyotis scandens', 'Sarcostemma brevistigma', 'Sarcostemma brevistigma', 'Sarcostemma brevistigma',
            'Correa .', 'Correa Roxb', 'Neolamarckia cadamba', 'Neolamarckia cadamba', 'Neolamarckia cadamba',
            'Acorus calamus', 'Abies balsamea', 'Abies balsamea', 'Abies grandis', 'Abies grandis', 'Abies grandis',
            'Pinus banksiana', 'Vaccinium vitis-idaea', 'Diospyros melanoxylon', 'Diospyros melanoxylon',
            'Diospyros melanoxylon', 'Oroxylum indicum', 'Oroxylum indicum', 'Oroxylum indicum', 'Alnus incana',
            'Alnus rubra', 'Curcuma domestica', 'Curcuma longa', 'Curcuma longa', 'Curcuma longa', 'Curcuma longa',
            'Curcuma longa', 'Curcuma longa', 'Curcuma longa', 'Curcuma longa', 'Curcuma longa', 'Cyperus scariosus',
            'Cyperus rotundus', 'Cyperus scariosus', 'Cyperus rotundus', 'Withania somnifera', 'Withania somnifera',
            'Withania somnifera', 'Withania somnifera', 'Withania somnifera', 'Withania somnifera',
            'Withania somnifera', 'Withania somnifera', 'Populus tremuloides', 'Populus tremuloides',
            'Brassica campestris', 'Brassica campestris', 'Brassica juncea', 'Brassica juncea', 'Brassica juncea',
            'Litsea :', 'Litsea one', 'Litsea species', 'Litsea species', 'Litsea species', 'Litsea species',
            'Litsea Species', 'Litsea show', 'Litsea comprises', 'Litsea species', 'Litsea pharmacological',
            'Litsea species', 'Symphoricarpos albus', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica',
            'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica',
            'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica', 'Azadirachta indica',
            'Azadirachta Indica', 'Picea mariana', 'Picea glauca', 'Kalmia angustifolia', 'Solanum americanum',
            'Casearia esculenta', 'Eclipta prostrata', 'Cajanus cajan', 'Morus indica', 'Morus alba', 'Morus alba',
            'Morus alba', 'Justicia secunda', 'Osyris wightiana', 'Lagerstroemia speciosa', 'Sarracenia purpurea',
            'Sambucus racemosa', 'Tanacetum nubigenum', 'Tanacetum nubigenum', 'Tanacetum nubigenum',
            'Tanacetum nubigenum', 'Pterocarpus marsupium', 'Pterocarpus marsupium', 'Pterocarpus santalinus',
            'Pterocarpus santalinus', 'Pterocarpus marsupium', 'Pterocarpus marsupium', 'Pterocarpus marsupium',
            'Pterocarpus marsupium', 'Pterocarpus marsupium', 'Pterocarpus marsupium', 'Pterocarpus marsupium',
            'Pterocarpus marsupium', 'Anacyclus pyrethrum', 'Solidago canadensis', 'Lycopodium clavatum',
            'Paederia foetida', 'Paederia foetida', 'Cicer arietum', 'Artemisia pallens', 'Artemisia pallens',
            'Jatropha curcus', 'Jatropha curcus', 'Cucumis sativus', 'Cucumis melo', 'Cucumis melo',
            'Cucumis prophetarum', 'Cucumis prophetarum', 'Areca catechu', 'Benincasa hispida', 'Benincasa hispida',
            'Benincasa hispida', 'Benincasa hispida', 'Benincasa hispida', 'Benincasa hispida', 'Nerium oleander',
            'Trichosanthes cucumerina', 'Trichosanthes dioica', 'Hydnocarpus wightiana', 'Hydnocarpus wightiana',
            'Quercus garryana', 'Quercus alba', 'Ayapana triplinervis', 'Beyeria leshnaultii', 'Mahonia spp.',
            'Ocimum sanctum', 'Ocimum tenuiflorum', 'Ocimum gratissimum', 'Ocimum sanctum', 'Ocimum sanctum',
            'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum', 'Ocimum sanctum',
            'Ocimum tenuiflorum', 'Ocimum tenuiflorum', 'Ocimum tenuiflorum', 'Ocimum sanctum', 'Ocimum sanctum',
            'Ocimum sanctum', 'Ocimum sanctum.Exploration', 'Ocimum sanctum', 'Ocimum sanctum',
            'Andrographis paniculata', 'Andrographis paniculata', 'Andrographis paniculata', 'Andrographis paniculata',
            'Andrographis paniculata', 'Zingiber officinale', 'Zingiber officinale', 'Tinospora cordifolia',
            'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia',
            'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia',
            'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia',
            'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cardifolia',
            'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia',
            'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora cordifolia', 'Tinospora includes',
            'Tinospora species', 'Tinospora species', 'Tinospora reveal', 'Tinospora cordifolia',
            'Symplocos cochinchinensis', 'Melia azedarach', 'Melia azedarach', 'Melia azaderach', 'Stevia rebaudiana',
            'Stevia rebaudiana', 'Tragia involucrata', 'Momordica charantia', 'Momordica charantia',
            'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia',
            'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia',
            'Momordica charantia', 'Momordica charantia', 'Momordica charantia', 'Momordica charantia',
            'Momordica charantia', 'Musa paradisiaca', 'Musa paradisiaca', 'Musa AAA', 'Musa AAA', 'Musa AAA',
            'Musa AAA', 'Bixa orellana', 'Bixa orellana', 'Bixa orellana', 'Biophytum sensitivum',
            'Biophytum sensitivum', 'Pseudotsuga menziesii', 'Pseudotsuga menziesii', 'Pseudotsuga menziesii',
            'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre',
            'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre',
            'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre', 'Gymnema sylvestre',
            'Gymnema sylvestre', 'Phyllanthus emblica', 'Phyllanthus emblica', 'Phyllanthus emblica',
            'Phyllanthus emblica', 'Phyllanthus amarus', 'Phyllanthus amarus', 'Phyllanthus amarus',
            'Phyllanthus niruri', 'Rubus spectabilis', 'Rubus spectabilis', 'Abutilon indicum', 'Triticum aestivum',
            'Petroselinum crispum', 'Mangifera indica', 'Gynura cusimbua', 'Swertia chirayita', 'Swertia chirayita',
            'Swertia cordata', 'Swertia chirayita', 'Swertia cordata', 'Swertia chirayita', 'Swertia cordata',
            'Swertia chirayita', 'Swertia species', 'Swertia contain', 'Swertia chirayita', 'Swertia cordata',
            'Swertia chirayita', 'Cinnamomum tamala', 'Cinnamomum verum', 'Swietenia mahagoni', 'Swietenia mahagoni',
            'Mucuna prurita', 'Mucuna pruriens', 'Mucuna pruriens', 'Mucuna pruriens', 'Mucuna pruriens',
            'Caesalpinia bonducella', 'Malus fusca', 'Costus igneus', 'Costus speciosus', 'Costus speciosus',
            'Dendrocalamus hamiltonii', 'Zanthoxylum alatum', 'Zanthoxylum alatum', 'Zanthoxylum alatum',
            'Gaultheria hispidula', 'Salacia reticulata', 'Salacia (', 'Salacia oblonga', 'Salacia oblonga',
            'Coptis chinensis', 'Moringa oleifera', 'Moringa oleifera', 'Moringa oleifera', 'Moringa oleifera',
            'Moringa pterygosperma', 'Moringa oleifera', 'Moringa oleifera', 'Oplopanax horridus', 'Oplopanax horridus',
            'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos', 'Aegle marmelos',
            'Aegle marmelos', 'Aegle marmelose', 'Aegle marmelos', 'Aegle marmelos', 'Allium sativum', 'Allium sativum',
            'Allium sativum', 'Allium sativum', 'Allium carolinianum', 'Allium sativum', 'Allium sativum',
            'Allium sativum', 'Allium sativum', 'Allium sativum', 'Allium cepa', 'Allium sativum', 'Rhamnus purshianus',
            'Cyclea peltata', 'Bambusa dendrocalamus', 'Blumeopsis flava', 'Larix laricina', 'Larix laricina',
            'Larix laricina', 'Larix laricina', 'Larix laricina', 'Saba ,', 'Murraya koenigii', 'Murraya koenigii',
            'Murraya koeingii', 'Rhus hirta', 'Hemidesmus indicus', 'Hemidesmus indicus', 'Psidium guajava',
            'Mentha piperitae', 'Phaseolus mungo', 'Phaseolus mungo', 'Phaseolus mungo', 'Phaseolus aureus',
            'Linum usitatisumum', 'Linum usitatisumum', 'Linum usitatisumum', 'Clerodendrum glandulosum',
            'Clerodendrum glandulosum', 'Centella asiatica', 'Centella asiatica', 'Centella asiatica',
            'Boerhavia diffusa', 'Boerhavia diffusa', 'Trigonella foenum', 'Trigonella foenum', 'Trigonella foenum',
            'Trigonella seed', 'Trigonella seed', 'Trigonella foenum', 'Trigonella foenum', 'Trigonella foenum',
            'Trigonella foenum', 'Trigonella foenum', 'Trigonella foenum-graceum', 'Trigonella foenum',
            'Trigonella foenum', 'Trigonella seed', 'Trigonella seed', 'Trigonella seed', 'Trigonella seed',
            'Adansonia digitata', 'Rauvolfia serpentina', 'Streblus asper', 'Streblus asper', 'Cornus nuttallii',
            'Cornus stolonifera', 'Vinca rosea', 'Vinca rosea', 'Vinca rosea', 'Blumea aromatica', 'Blumea aromatica',
            'Blumea species', 'Terminalia arjuna', 'Terminalia chebula', 'Terminalia belerica', 'Terminalia bellirica',
            'Terminalia chebula', 'Terminalia bellirica', 'Terminalia amongst', 'Terminalia species',
            'Terminalia chebula', 'Terminalia species', 'Terminalia species', 'Terminalia species',
            'Terminalia species', 'Terminalia species', 'Terminalia arjuna', 'Terminalia bellerica',
            'Terminalia catappa', 'Terminalia species', 'Terminalia bellerica', 'Terminalia bellerica',
            'Terminalia chebula', 'Santalum spicatum', 'Syzygium cumin', 'Syzygium jambolanum', 'Syzygium jambolanum',
            'Syzygium cumini', 'Syzygium cumini', 'Syzygium cumini', 'Syzygium cumini', 'Syzygium cumini',
            'Euphorbia nivulia', 'Euphorbia drummondii', 'Euphorbia drummondii', 'Premna integrifolia',
            'Schisandra grandiflora', 'Schisandra grandiflora', 'Glycyrrhiza glabra', 'Prunus emarginata',
            'Prunus emarginata', 'Catharanthus roseus', 'Catharanthus roseus', 'Catharanthus roseus',
            'Boswellia serrata', 'Saponaria officinalis', 'Coccinia indica', 'Coccinia indica', 'Coccinia indica',
            'Coccinia grandis', 'Coccinia indica', 'Berberis aristata']

diseas_dict = {'cancer': cancer,
               'fever': fever,
               'arthidis': arthidis,
               'diabetes': diabetes}

all_4_plants = []
for i in diabetes:
    if i in cancer:
        if i in fever:
            if i in arthidis:
                all_4_plants.append(i)

plants_dict = {}
for i in all_4_plants:
    if i in plants_dict:
        plants_dict[i] += 1
    else:
        plants_dict.update({i: 1})

plants_dict = sorted(plants_dict.items(), key=lambda x: x[1], reverse=True)

x = [i[0] for i in plants_dict]
y = [i[1] for i in plants_dict]
#
# # ============================ abstracts sepration based on disaes =================
#
from matplotlib import pyplot as plt

plt.barh(x, y)
plt.title('Common Plants In All Disease')
plt.ylabel('Plant Name')
plt.xlabel('Number of Occurrence')
# plt.yticks(rotation=90)
plt.show()
#


# ================================================= find the plants in abstracts ==============================

import glob

files = glob.glob('/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/ALL/*.txt')

all_plants = ['Curcuma longa', 'Tinospora cordifolia', 'Withania somnifera', 'Ocimum sanctum', 'Oplopanax horridus',
              'Acorus calamus']

list_of_diseas = [
    '/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/arthidis',
    '/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/cancer',
    '/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/diabetes',
    '/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/fever'

]

plant_list = diabetes
plant_list = set(plant_list)

abstract_count = {}
for plant in plant_list:
    abstract_count.update({plant: 0})
    for j in files:
        try:
            with open(j, encoding='utf-8') as f:
                text = f.read()
        except:
            try:
                with open(j, encoding='utf-16') as f:
                    text = f.read()
            except:
                with open(j, encoding='latin-1') as f:
                    text = f.read()

        if plant in text:
            abstract_count[plant] += 1

abstr_cont = sorted(abstract_count.items(), key=lambda x: x[1], reverse=True)[:20]

x = [i[0] for i in abstr_cont]
y = [i[1] for i in abstr_cont]

#
from matplotlib import pyplot as plt

plt.barh(x, y)
plt.title('Individual Plant occurrence in Abstracts')
plt.ylabel('Plant Name')
plt.xlabel('Number of Abstracts')
# plt.yticks(rotation=90)
plt.show()

plt.barh(x, y)
plt.title('Individual Plant occurrence in Abstracts')
plt.ylabel('Plant Name')
plt.xlabel('Number of Abstracts')
# plt.yticks(rotation=90)
plt.show()

# ====================================== common plants in indivula disease wise abstracts ============================


files = glob.glob('/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/ALL/*.txt')

all_plants = ['Curcuma longa', 'Tinospora cordifolia', 'Withania somnifera', 'Ocimum sanctum', 'Oplopanax horridus',
              'Acorus calamus']

list_of_diseas = [
    '/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/arthidis',
    '/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/cancer',
    '/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/diabetes',
    '/mnt/dash/Alpha_Share/Automation_Team/Tamil/NLP_learning/Plant_names/own_script/fever'

]

temp = []
for dis in list_of_diseas:
    files = glob.glob(dis + '/*.txt')

    abstract_count = {}
    for plant in all_plants:
        abstract_count.update({plant: 0})
        for j in files:
            try:
                with open(j, encoding='utf-8') as f:
                    text = f.read()
            except:
                try:
                    with open(j, encoding='utf-16') as f:
                        text = f.read()
                except:
                    with open(j, encoding='latin-1') as f:
                        text = f.read()

            if plant in text:
                abstract_count[plant] += 1

    temp.append(abstract_count)

final_dcit = {}
for i in all_plants:
    final_dcit.update({i: []})
    for t in temp:
        final_dcit[i].append(t[i])

import numpy as np
import matplotlib.pyplot as plt

N = 6
ind = np.arange(N)  # the x locations for the groups
width = 0.1  # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

yvals = [2, 2, 1,1, 1, 1]
rects1 = ax.bar(ind, yvals, width, color='g')
zvals = [1, 3, 14, 2, 1, 2]
rects2 = ax.bar(ind + width, zvals, width, color='b')
y1vals = [6, 13, 4, 10, 1, 1]
rects3 = ax.bar(ind + width*2, y1vals, width, color='y')
z1vals = [1, 1, 1, 4, 3, 3]
rects4 = ax.bar(ind + width*3, z1vals, width, color='r')


ax.set_ylabel('Number of Abstracts Used')
ax.set_xlabel('Plant Names')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(all_plants)
ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('Arthritis', 'Cancer', 'Diabetes', 'Fever'))


def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.02 * h, '%d' % int(h),
                ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
plt.title('Common Plants Extraction in Multiple Disease Abstracts')
plt.show()
