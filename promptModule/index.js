import { prompts } from "./prompts/index.js";

export function createPrompts(version, msg) {
  const template = prompts[version];
  if (template) {
    return template(msg);
  } else {
    throw new Error(`version "${version}" not found.`);
  }
}
