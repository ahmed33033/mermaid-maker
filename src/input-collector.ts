import * as core from "@actions/core";
import { action_input_type, action_input } from "./input-schema.js";
import * as z from "zod";

export async function input_collector(): Promise<action_input_type | {}> {
    try {
        const convert_existing = core.getBooleanInput("convert_existing", { required: false });
        const input_dir = core.getInput("input_dir", { required: false });
        const input_file_extension = core.getInput("input_file_extension", { required: false });
        const output_dir = core.getInput("output_dir", { required: false });
        const output_file_extension = core.getInput("output_file_extension", { required: false });

        return action_input.parse({ convert_existing, input_dir, input_file_extension, output_dir, output_file_extension })
    }
    catch (e) {
        if (e instanceof z.ZodError) {
            core.setFailed(z.prettifyError(e))
        }
        else if (e instanceof Error) {
            core.setFailed(e.message)
        }
        else {
            core.setFailed("Sorry, an unknown error occured.")
        }
        return {};
    }
}