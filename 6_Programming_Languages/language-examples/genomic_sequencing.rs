use std::collections::HashMap;

#[derive(Debug, Clone)]
pub struct DnaSequence {
    sequence: String,
    quality_scores: Vec<u8>,
}

impl DnaSequence {
    pub fn new(sequence: String, quality_scores: Vec<u8>) -> Self {
        DnaSequence {
            sequence,
            quality_scores,
        }
    }

    pub fn reverse_complement(&self) -> String {
        self.sequence
            .chars()
            .rev()
            .map(|base| match base {
                'A' => 'T',
                'T' => 'A',
                'G' => 'C',
                'C' => 'G',
                _ => base,
            })
            .collect()
    }

    pub fn gc_content(&self) -> f64 {
        let gc_count = self.sequence.chars()
            .filter(|&base| base == 'G' || base == 'C')
            .count();
        gc_count as f64 / self.sequence.len() as f64 * 100.0
    }

    pub fn base_composition(&self) -> HashMap<char, usize> {
        let mut composition = HashMap::new();
        for base in self.sequence.chars() {
            *composition.entry(base).or_insert(0) += 1;
        }
        composition
    }

    pub fn translate(&self) -> String {
        let codon_table: HashMap<&str, char> = [
            ("TTT", 'F'), ("TTC", 'F'), ("TTA", 'L'), ("TTG", 'L'),
            ("TCT", 'S'), ("TCC", 'S'), ("TCA", 'S'), ("TCG", 'S'),
            ("TAT", 'Y'), ("TAC", 'Y'), ("TAA", '*'), ("TAG", '*'),
            ("TGT", 'C'), ("TGC", 'C'), ("TGA", '*'), ("TGG", 'W'),
            ("CTT", 'L'), ("CTC", 'L'), ("CTA", 'L'), ("CTG", 'L'),
            ("CCT", 'P'), ("CCC", 'P'), ("CCA", 'P'), ("CCG", 'P'),
            ("CAT", 'H'), ("CAC", 'H'), ("CAA", 'Q'), ("CAG", 'Q'),
            ("CGT", 'R'), ("CGC", 'R'), ("CGA", 'R'), ("CGG", 'R'),
            ("ATT", 'I'), ("ATC", 'I'), ("ATA", 'I'), ("ATG", 'M'),
            ("ACT", 'T'), ("ACC", 'T'), ("ACA", 'T'), ("ACG", 'T'),
            ("AAT", 'N'), ("AAC", 'N'), ("AAA", 'K'), ("AAG", 'K'),
            ("AGT", 'S'), ("AGC", 'S'), ("AGA", 'R'), ("AGG", 'R'),
            ("GTT", 'V'), ("GTC", 'V'), ("GTA", 'V'), ("GTG", 'V'),
            ("GCT", 'A'), ("GCC", 'A'), ("GCA", 'A'), ("GCG", 'A'),
            ("GAT", 'D'), ("GAC", 'D'), ("GAA", 'E'), ("GAG", 'E'),
            ("GGT", 'G'), ("GGC", 'G'), ("GGA", 'G'), ("GGG", 'G'),
        ].iter().cloned().collect();

        self.sequence
            .chars()
            .collect::<Vec<char>>()
            .chunks(3)
            .map(|codon| {
                if codon.len() == 3 {
                    let codon_str: String = codon.iter().collect();
                    codon_table.get(codon_str.as_str()).unwrap_or(&'X').clone()
                } else {
                    'X'
                }
            })
            .collect()
    }
}

#[derive(Debug)]
pub struct SequencingRead {
    id: String,
    sequence: DnaSequence,
    paired: bool,
}

impl SequencingRead {
    pub fn new(id: String, sequence: String, quality_scores: Vec<u8>, paired: bool) -> Self {
        SequencingRead {
            id,
            sequence: DnaSequence::new(sequence, quality_scores),
            paired,
        }
    }

    pub fn quality_filter(&self, min_quality: u8) -> bool {
        self.sequence.quality_scores.iter()
            .all(|&score| score >= min_quality)
    }
}

pub fn simulate_illumina_sequencing(genome: &str, read_length: usize, coverage: f64) -> Vec<SequencingRead> {
    let mut reads = Vec::new();
    let num_reads = ((genome.len() as f64 * coverage) / read_length as f64) as usize;
    
    for i in 0..num_reads {
        let start_pos = i * read_length % (genome.len() - read_length + 1);
        let end_pos = start_pos + read_length;
        
        if end_pos <= genome.len() {
            let read_seq = genome[start_pos..end_pos].to_string();
            let quality_scores = vec![30; read_length]; // Phred score 30
            
            let read = SequencingRead::new(
                format!("read_{}", i),
                read_seq,
                quality_scores,
                false,
            );
            reads.push(read);
        }
    }
    
    reads
}

fn main() {
    let sample_sequence = "ATGGCGTACGATCGATCGATCGATCGATCGTAG".to_string();
    let quality_scores = vec![35; sample_sequence.len()];
    
    let dna = DnaSequence::new(sample_sequence, quality_scores);
    
    println!("Original sequence: {}", dna.sequence);
    println!("Reverse complement: {}", dna.reverse_complement());
    println!("GC content: {:.2}%", dna.gc_content());
    println!("Base composition: {:?}", dna.base_composition());
    println!("Protein translation: {}", dna.translate());
    
    let genome = "ATGGCGTACGATCGATCGATCGATCGATCGTAGCCCGGGAAATTTCCCGGGAAATTTCCCGGGAAATTT";
    let reads = simulate_illumina_sequencing(genome, 20, 2.0);
    
    println!("\nSimulated {} Illumina reads:", reads.len());
    for (i, read) in reads.iter().take(5).enumerate() {
        println!("Read {}: {}", i + 1, read.sequence.sequence);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_reverse_complement() {
        let dna = DnaSequence::new("ATCG".to_string(), vec![30; 4]);
        assert_eq!(dna.reverse_complement(), "CGAT");
    }

    #[test]
    fn test_gc_content() {
        let dna = DnaSequence::new("GCGC".to_string(), vec![30; 4]);
        assert_eq!(dna.gc_content(), 100.0);
    }

    #[test]
    fn test_translation() {
        let dna = DnaSequence::new("ATGGCGTAG".to_string(), vec![30; 9]);
        assert_eq!(dna.translate(), "MA*");
    }
}