import Anthropic from "@anthropic-ai/sdk";
import dotenv from "dotenv";
import { createPrompts } from "./promptModule/index.js";
import clipboardy from "clipboardy";

import { fileURLToPath } from "url";
import path from "path";
import fs from "fs";

dotenv.config();

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

const mainWithFile = async (version) => {
  const getArgument = () => process.argv[2];
  const getRootPath = () => path.dirname(fileURLToPath(import.meta.url));
  const getAbsolutePath = (filePath, relativePath) =>
    path.resolve(filePath, relativePath);
  const getFile = (filePath) => fs.readFileSync(filePath, "utf8");
  const isFileExists = (filePath) => fs.existsSync(filePath);

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

const mainWithClipboard = async (version) => {
  const clipboardContent = clipboardy.readSync();

  if (!clipboardContent && clipboardContent.length <= 10) {
    console.warn("클립보드에 내용이 없습니다.");
    return;
  }

  const tromptMsg = createPrompts(version, clipboardContent);
  const response = await sendMsg(tromptMsg);
  console.log(response.content[0].text);
};

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

(async function run() {
  const versions = ["version0", "version1", "version2", "version3"];

  for (const version of versions) {
    console.log("--------------");
    console.log(`${version} 검사 시작`);
    mainWithClipboard(version);
    await sleep(50000);
  }
})();
