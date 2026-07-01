import * as z from "zod";

export const action_input = z.object({
    convert_existing: z.coerce.boolean(),
    input_dir: z.string(),
    input_file_extension: z.string().max(5),
    output_dir: z.string(),
    output_file_extension: z.literal(["svg", "png", "pdf"])
})

export type action_input_type = z.infer<typeof action_input>;
