def reassemble_file(parts, output_file):
    with open(output_file, 'wb') as f_out:
        for part in parts:
            with open(part, 'rb') as f_in:
                f_out.write(f_in.read())

# List the part files you created
parts = ['best.pt_part_1', 'best.pt_part_2']  # Update as needed
reassemble_file(parts, 'best.pt')
