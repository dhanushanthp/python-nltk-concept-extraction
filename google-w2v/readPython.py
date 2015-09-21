import gensim.models as gm;

# model = gm.Word2Vec.load_word2vec_format('wiki-2015-dumb-trained.bin', binary=True)
# model = gm.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
model = gm.Word2Vec.load_word2vec_format('freebase-vectors-skipgram1000.bin', binary=True)

def getRelatedConcepts(user_input,topCount):
    list = [];
    print("input : " + user_input);
#     user_input = input("Some input please: ")
#     if user_input == "exit":
#         break;
    words = user_input.split();
    try:
        json = '{"concepts": ['
#         values = model.most_similar(positive=words, topn=int(topCount));
        values = model.most_similar(positive=words, topn=int(topCount));
        for obj in values:
            concept = obj[0].replace('_', ' ');
            list.append(concept.strip())
#             print (concept.strip());
        for concept in set(list):
            json = json + '"' + concept + '",';
        json = json + ']}';
        json = json.replace(',]}', ']}');
        return json;
    except KeyError:
#         print ('I got a KeyError - reason');
        return '{"concepts": [\'related Concepts not found\']}';
    except Exception:
#         print ("error.....");
        return '{"concepts": [\'related concepts not found error\']}';
        
#getRelatedConcepts("java",1000);
