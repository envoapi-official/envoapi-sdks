import { EnvoAPI } from 'envoapi';

const client = new EnvoAPI({ baseUrl: process.env.ENVOAPI_BASE_URL });
const result = await client.profiles.getPosts({ username: process.env.ENVOAPI_USERNAME ?? 'alice' });
console.log(JSON.stringify({posts: result.body.data.posts, creditCost: result.body.meta.creditCost}));
