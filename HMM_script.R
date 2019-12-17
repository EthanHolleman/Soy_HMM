library('HMM')

setwd("/home/ethan/Desktop/HMM")

# Read in the emmission and transition probs created from included python
# script. Make sure to change the current working directory above

emm_matrix <- data.matrix(read.csv(file = 'Emissions.csv', header = FALSE))
trans_matrix <- data.matrix(read.csv(file = 'Transitions.csv', header = FALSE))

start_probs <- c(trans_matrix[1, ])  # start probs == genomic transition probs
states <- c("G", "S", "I")  # G = genomic seq, S = solo element, I = intact element
symbols <- c("A", "T", "G", "C", "N")

# init the HMM with all probability data
HMM <- initHMM(states, symbols, start_probs, trans_matrix, emm_matrix)


chr1 <- read.csv('/home/ethan/Desktop/HMM/GMax1.1_assembly/chr1.fna', sep = '\n',
                 stringsAsFactors = FALSE)

chr1_vector <- unlist(strsplit(chr1[,1], ''))

# calculate states using HMM and viterbi algo
HMM_Viterbi_Chr1 <- viterbi(HMM, chr1_vector)