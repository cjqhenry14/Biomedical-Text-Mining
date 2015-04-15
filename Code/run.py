import os
from shutil import copyfile

def exe_lda_10():
	pre_cmd ="./main   --ntopics=10   --mode=fit   --rng_seed=0   --initialize_lda=true   --corpus_prefix=example1/dtm   --outname=example1/model_run   --top_chain_var=0.005   --alpha=0.01   --lda_sequence_min_iter=6   --lda_sequence_max_iter=20   --lda_max_em_iter=10"
	os.system(pre_cmd)
	# propath = "/Users/chenjiaqi/Desktop/SB1/Computational Biology/biopro/"
	# copyfile(propath + "art_topic/model-final.twords", propath + "year_topic/" + year + "/" + year +".twords")
	# copyfile(propath + "art_topic/model-final.phi", propath + "year_topic/" + year + "/" + year + ".phi")
	# copyfile(propath + "art_topic/model-final.tassign", propath + "year_topic/" + year + "/" + year + ".tassign")
	# copyfile(propath + "art_topic/model-final.theta", propath + "year_topic/" + year + "/" + year + ".theta")
	# copyfile(propath + "art_topic/wordmap.txt", propath + "year_topic/" + year + "/wordmap.txt")

	# propath2 = "/Users/chenjiaqi/Desktop/SB1/Computational\ Biology/biopro/art_topic/"
	# rmcmd = "rm " + propath2 + "*.theta " + propath2 + "*.tassign " + propath2 + "wordmap.txt " + propath2 + "*.phi " + propath2 + "*.twords " + propath2 + "*.others " 
	# os.system(rmcmd)
def exe_lda_11():
	pre_cmd ="./main   --ntopics=10   --mode=fit   --rng_seed=0   --initialize_lda=true   --corpus_prefix=example2/dtm   --outname=example2/model_run   --top_chain_var=0.005   --alpha=0.01   --lda_sequence_min_iter=6   --lda_sequence_max_iter=20   --lda_max_em_iter=10"
	os.system(pre_cmd)
def exe_lda_12():
	pre_cmd ="./main   --ntopics=10   --mode=fit   --rng_seed=0   --initialize_lda=true   --corpus_prefix=example3/dtm   --outname=example3/model_run   --top_chain_var=0.005   --alpha=0.01   --lda_sequence_min_iter=6   --lda_sequence_max_iter=20   --lda_max_em_iter=10"
	os.system(pre_cmd)
def exe_lda_13():
	pre_cmd ="./main   --ntopics=10   --mode=fit   --rng_seed=0   --initialize_lda=true   --corpus_prefix=example4/dtm   --outname=example4/model_run   --top_chain_var=0.005   --alpha=0.01   --lda_sequence_min_iter=6   --lda_sequence_max_iter=20   --lda_max_em_iter=10"
	os.system(pre_cmd)
def exe_lda_14():
	pre_cmd ="./main   --ntopics=10   --mode=fit   --rng_seed=0   --initialize_lda=true   --corpus_prefix=example5/dtm   --outname=example5/model_run   --top_chain_var=0.005   --alpha=0.01   --lda_sequence_min_iter=6   --lda_sequence_max_iter=20   --lda_max_em_iter=10"
	os.system(pre_cmd)
def exe_lda_15():
	pre_cmd ="./main   --ntopics=10   --mode=fit   --rng_seed=0   --initialize_lda=true   --corpus_prefix=example/dtm   --outname=example/model_run   --top_chain_var=0.005   --alpha=0.01   --lda_sequence_min_iter=6   --lda_sequence_max_iter=20   --lda_max_em_iter=10"
	os.system(pre_cmd)


if (__name__ == '__main__'):
	# exe_lda_10()
	exe_lda_11()
	exe_lda_12()
	exe_lda_13()
	exe_lda_14()
	exe_lda_15()
    








