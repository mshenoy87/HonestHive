import { backendLookup } from "../lookup";

export function loadWaggles(username, callback, nextURL) {

  let endpoint = "/waggles/";
  // get method to show waggles
  if (username) {
    endpoint = `/waggles/?username=${username}`;
  }

  if (nextURL !== null && nextURL !== undefined) {
    endpoint = nextURL.replace("http://localhost:8000/api", "");
  }
  backendLookup("GET", endpoint, callback);
}

export function apiWaggleFeed(callback, nextURL) {

  let endpoint = "/waggles/feed/";

  if (nextURL !== null && nextURL !== undefined) {
    endpoint = nextURL.replace("http://localhost:8000/api", "");
  }
  backendLookup("GET", endpoint, callback);
}

export function createWaggle(newWaggle, callback) {
  // post method to update the list of waggles
  backendLookup("POST", "/waggles/create/", callback, {waggleText: newWaggle});
}

export function waggleAction(waggle_id, action, callback) {
  // post method to update the list of waggles
  backendLookup("POST", "/waggles/action/", callback, {id: waggle_id, action: action});
}

export function waggleDetail(waggleID, callback) {
  backendLookup("GET", `/waggles/${waggleID}/`, callback);
}