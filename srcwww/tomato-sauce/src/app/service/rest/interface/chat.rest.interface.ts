import { Injectable } from '@angular/core';
import { HttpClient, HttpDownloadProgressEvent, HttpEvent, HttpEventType } from '@angular/common/http';
import { ChatConversation, ChatEntry, RagLookup, RagReference } from '../../../data/conversation.data';
import { RootRestService } from '../base.rest.interface';
import { result_is_ok, RestResult } from '../../../data/result.data';

@Injectable({
    providedIn: 'root'
})
export class ChatRestInterface {
    static CHAT_URL = 'llm/chat';
    static RAG_LOOKUP_URL = 'llm/references';

    conversation: ChatConversation = {
        chats: [
        ],
        inject_rag: true
    };

    references: RagLookup[] = []

    constructor() {

    }

    clear_conversation() {
        this.references = [];
        this.conversation = {
            chats: [],
            inject_rag: true
        };
    }

    async chat(http: HttpClient, inject_rag: boolean, content: string) {
        this.conversation.inject_rag = inject_rag;
        this.conversation.chats.push({
            role: 'user',
            content: content
        });
        let new_message: ChatEntry = {
            role: 'assistant',
            content: ''
        };
        this.conversation.chats.push(new_message);

        http.post(RootRestService.url(ChatRestInterface.CHAT_URL), this.conversation, {
            observe: "events",
            responseType: "text",
            reportProgress: true
        }).subscribe({
            next: (event: HttpEvent<string>) => {
                if (event.type == HttpEventType.DownloadProgress) {
                    new_message.content = (
                        event as HttpDownloadProgressEvent
                    ).partialText + '...'
                } else if (event.type == HttpEventType.Response) {
                    new_message.content = (event.body ?? '')
                    if (inject_rag) {
                        this.get_references(http)
                    }
                }
            },
            error: (e) => {
                console.log(e)
                // TODO: Add Error Handling for Chats
            }
        })
    }

    async get_references(http: HttpClient) {
        http.get<RestResult>(RootRestService.url(ChatRestInterface.RAG_LOOKUP_URL)).subscribe({
            next: (event) => {
                if (result_is_ok(event)) {
                    this.references.push(event.body as RagLookup)
                } else {
                    console.warn('Get LLM References Errored')
                    console.log(event.body)
                    // TODO: Add Error Handling
                }
            },
            error: (e) => {
                console.error("ERRORED");
                console.log(e)
                // TODO: Add Error Handling
            }
        })
    }

    list_references(index: number): RagReference[] {
        if (index == null || index < 0 || index >= this.references.length) {
            return []
        }
        return this.references[index].lookups;
    }
}