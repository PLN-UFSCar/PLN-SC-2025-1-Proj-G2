#######

def load_terms(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return set(line.strip().lower() for line in f if line.strip())

def count_correct_terms(output_path, reference_path, term_set):
    total_found = 0
    correct = 0

    with open(output_path, 'r', encoding='utf-8') as sys_out, \
         open(reference_path, 'r', encoding='utf-8') as refs:
        
        for hypo_line, ref_line in zip(sys_out, refs):
            hypo_terms = [term for term in term_set if term in hypo_line.lower()]
            total_found += len(hypo_terms)
            correct += sum(term in ref_line.lower() for term in hypo_terms)

    return correct, total_found

# Caminhos
terms_file = 'termos.txt'
output_file = './corpus/corpus10k.output.pt'
reference_file = './corpus/corpus10k.clean.pt'

# Cálculo
terms = load_terms(terms_file)
correct, total = count_correct_terms(output_file, reference_file, terms)

precision = correct / total if total > 0 else 0
print(f'Precisão Terminológica: {precision:.2%} ({correct}/{total})')