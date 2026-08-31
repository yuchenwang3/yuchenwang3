import fs from "node:fs";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { user_record: userRecord } = require("NeteaseCloudMusicApi");

const uid = process.env.NETEASE_UID;
const musicU = process.env.NETEASE_MUSIC_U;

if (!uid || !musicU) {
  throw new Error("NETEASE_UID and NETEASE_MUSIC_U are required");
}

const response = await userRecord({
  uid,
  type: 1,
  cookie: { MUSIC_U: musicU },
});

const weekly = response?.body?.weekData;
if (!Array.isArray(weekly) || weekly.length === 0) {
  throw new Error(
    `No weekly listening data returned (code ${response?.body?.code ?? "unknown"})`,
  );
}

const tracks = weekly.slice(0, 5).map((entry) => ({
  title: entry.song?.name || "Unknown track",
  artist:
    entry.song?.ar
      ?.map((artist) => artist.name)
      .filter(Boolean)
      .join(" / ") ||
    entry.song?.artists
      ?.map((artist) => artist.name)
      .filter(Boolean)
      .join(" / ") ||
    "Unknown artist",
  plays: Number(entry.playCount || 0),
}));

const escapeXml = (value) =>
  String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&apos;");

const truncate = (value, max) => {
  const chars = Array.from(String(value));
  return chars.length > max ? `${chars.slice(0, max - 1).join("")}…` : value;
};

const maxPlays = Math.max(...tracks.map((track) => track.plays), 1);
const rows = tracks
  .map((track, index) => {
    const y = 34 + index * 48;
    const width = Math.max(8, Math.round((372 * track.plays) / maxPlays));
    const rank = String(index + 1).padStart(2, "0");
    return `      <g transform="translate(0 ${y})">
        <text x="0" y="15" font-size="14" font-weight="650">${rank}</text><text x="35" y="15" font-size="14" font-weight="650">${escapeXml(truncate(track.title, 29))}</text><text x="444" y="15" text-anchor="end" font-family="JetBrains Mono, SFMono-Regular, Consolas, monospace" font-size="12" font-weight="700">${track.plays}</text>
        <rect x="35" y="26" width="372" height="4" rx="2" fill="#d9e1ed"/><rect x="35" y="26" width="${width}" height="4" rx="2" fill="url(#accent)"/>
        <text x="35" y="45" font-size="10.5" fill="#6b7b92">${escapeXml(truncate(track.artist, 42))}</text>
      </g>`;
  })
  .join("\n");

const weeklyGroup = `    <g transform="translate(410 42)">
      <text x="0" y="12" font-family="JetBrains Mono, SFMono-Regular, Consolas, monospace" font-size="11" font-weight="700" letter-spacing="1.4" fill="#566782">THIS WEEK / MOST PLAYED</text>
      <text x="444" y="12" text-anchor="end" font-family="JetBrains Mono, SFMono-Regular, Consolas, monospace" font-size="10" font-weight="650" fill="#76869d">PLAYS</text>

${rows}
    </g>`;

const sourcePath = "assets/music-card.svg";
const outputPath = "dist/music-card.svg";
let svg = fs.readFileSync(sourcePath, "utf8");
const sectionStart = svg.lastIndexOf('    <g transform="translate(410 42)">');
const sectionEnd = svg.lastIndexOf("    </g>\n  </g>\n</svg>");

if (sectionStart < 0 || sectionEnd < 0 || sectionEnd <= sectionStart) {
  throw new Error("Could not locate the music-card track section");
}

svg = `${svg.slice(0, sectionStart)}${weeklyGroup}\n${svg.slice(sectionEnd + 9)}`;
svg = svg
  .replace(
    /<title id="title">[^<]*<\/title>/,
    '<title id="title">Yuchen Wang&apos;s weekly listening snapshot</title>',
  )
  .replace(
    /<desc id="desc">[^<]*<\/desc>/,
    '<desc id="desc">11,410 tracks logged on NetEase Cloud, with the five most-played tracks from the latest week.</desc>',
  );

fs.writeFileSync(outputPath, svg);
console.log(`Published ${tracks.length} weekly tracks for NetEase user ${uid}`);
