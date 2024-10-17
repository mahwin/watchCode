import Anthropic from "@anthropic-ai/sdk";
import dotenv from "dotenv";
import { fileURLToPath } from "url";
import { createPrompts } from "./utils/createPropmts";
import path from "path";
import fs from "fs";

dotenv.config();

const getArgument = () => process.argv[2];

const getRootPath = () => path.dirname(fileURLToPath(import.meta.url));

const getAbsolutePath = (filePath, relativePath) =>
  path.resolve(filePath, relativePath);

const getFile = (filePath) => fs.readFileSync(filePath, "utf8");

const isFileExists = (filePath) => fs.existsSync(filePath);

const sendMsg = async (msg) => {
  const anthropic = new Anthropic({
    apiKey: process.env.CLAUDE_API_KEY,
  });

  return await anthropic.messages.create({
    model: "claude-3-5-sonnet-20240620",
    max_tokens: 1024,
    messages: [{ role: "user", content: msg }],
  });
};

const main = async () => {
  const relativePath = getArgument();

  if (!relativePath) {
    console.warn("검증하려는 대상이 없습니다.");
    return;
  }

  const rootPath = getRootPath();
  const absPath = getAbsolutePath(rootPath, relativePath);

  if (!isFileExists(absPath)) {
    console.warn("파일이 존재하지 않습니다.");
    return;
  }

  const userCode = getFile(absPath);
  const tromptMsg = createPrompts("version1", userCode);
  const response = await sendMsg(tromptMsg);
  console.log(response.content[0].text);
};

main();
