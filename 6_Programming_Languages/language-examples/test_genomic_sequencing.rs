#[path = "genomic_sequencing.rs"]
mod genomic_sequencing;

use genomic_sequencing::{DnaSequence, SequencingRead, simulate_illumina_sequencing};

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_dna_sequence_creation() {
        let seq = DnaSequence::new("ATCG".to_string(), vec![30, 31, 32, 33]);
        assert_eq!(seq.sequence, "ATCG");
        assert_eq!(seq.quality_scores, vec![30, 31, 32, 33]);
    }

    #[test]
    fn test_reverse_complement_basic() {
        let dna = DnaSequence::new("ATCG".to_string(), vec![30; 4]);
        assert_eq!(dna.reverse_complement(), "CGAT");
    }

    #[test]
    fn test_reverse_complement_complex() {
        let dna = DnaSequence::new("ATGGCGTACGAT".to_string(), vec![30; 12]);
        assert_eq!(dna.reverse_complement(), "ATCGTACGCCAT");
    }

    #[test]
    fn test_gc_content_zero() {
        let dna = DnaSequence::new("ATTA".to_string(), vec![30; 4]);
        assert_eq!(dna.gc_content(), 0.0);
    }

    #[test]
    fn test_gc_content_full() {
        let dna = DnaSequence::new("GCGC".to_string(), vec![30; 4]);
        assert_eq!(dna.gc_content(), 100.0);
    }

    #[test]
    fn test_gc_content_partial() {
        let dna = DnaSequence::new("ATGC".to_string(), vec![30; 4]);
        assert_eq!(dna.gc_content(), 50.0);
    }

    #[test]
    fn test_base_composition() {
        let dna = DnaSequence::new("AATTGGCC".to_string(), vec![30; 8]);
        let composition = dna.base_composition();
        assert_eq!(*composition.get(&'A').unwrap(), 2);
        assert_eq!(*composition.get(&'T').unwrap(), 2);
        assert_eq!(*composition.get(&'G').unwrap(), 2);
        assert_eq!(*composition.get(&'C').unwrap(), 2);
    }

    #[test]
    fn test_translation_start_codon() {
        let dna = DnaSequence::new("ATG".to_string(), vec![30; 3]);
        assert_eq!(dna.translate(), "M");
    }

    #[test]
    fn test_translation_stop_codon() {
        let dna = DnaSequence::new("ATGTAG".to_string(), vec![30; 6]);
        assert_eq!(dna.translate(), "M*");
    }

    #[test]
    fn test_translation_multiple_codons() {
        let dna = DnaSequence::new("ATGGCGTAG".to_string(), vec![30; 9]);
        assert_eq!(dna.translate(), "MA*");
    }

    #[test]
    fn test_translation_incomplete_codon() {
        let dna = DnaSequence::new("ATGGC".to_string(), vec![30; 5]);
        assert_eq!(dna.translate(), "MX");
    }

    #[test]
    fn test_sequencing_read_creation() {
        let read = SequencingRead::new(
            "read1".to_string(),
            "ATCG".to_string(),
            vec![35, 36, 37, 38],
            false
        );
        assert_eq!(read.id, "read1");
        assert_eq!(read.sequence.sequence, "ATCG");
        assert_eq!(read.paired, false);
    }

    #[test]
    fn test_quality_filter_pass() {
        let read = SequencingRead::new(
            "read1".to_string(),
            "ATCG".to_string(),
            vec![35, 36, 37, 38],
            false
        );
        assert!(read.quality_filter(30));
    }

    #[test]
    fn test_quality_filter_fail() {
        let read = SequencingRead::new(
            "read1".to_string(),
            "ATCG".to_string(),
            vec![25, 26, 27, 28],
            false
        );
        assert!(!read.quality_filter(30));
    }

    #[test]
    fn test_simulate_illumina_sequencing() {
        let genome = "ATGGCGTACGATCGATCGATCGATCGATCGTAG";
        let reads = simulate_illumina_sequencing(genome, 10, 1.0);
        
        assert!(!reads.is_empty());
        assert_eq!(reads[0].sequence.sequence.len(), 10);
        assert_eq!(reads[0].sequence.quality_scores.len(), 10);
        assert!(reads[0].sequence.quality_scores.iter().all(|&q| q == 30));
    }

    #[test]
    fn test_simulate_illumina_sequencing_coverage() {
        let genome = "ATGGCGTACGATCGATCGATCGATCGATCGTAG";
        let reads = simulate_illumina_sequencing(genome, 8, 2.0);
        
        let expected_reads = ((genome.len() as f64 * 2.0) / 8.0) as usize;
        assert_eq!(reads.len(), expected_reads);
    }

    #[test]
    fn test_comprehensive_workflow() {
        let original_seq = "ATGGCGTACGATCGATCGATCGATCGATCGTAG";
        let dna = DnaSequence::new(original_seq.to_string(), vec![35; original_seq.len()]);
        
        let reverse_comp = dna.reverse_complement();
        assert_eq!(reverse_comp.len(), original_seq.len());
        
        let gc_content = dna.gc_content();
        assert!(gc_content > 0.0 && gc_content <= 100.0);
        
        let protein = dna.translate();
        assert!(!protein.is_empty());
        
        let composition = dna.base_composition();
        let total_bases: usize = composition.values().sum();
        assert_eq!(total_bases, original_seq.len());
    }
}