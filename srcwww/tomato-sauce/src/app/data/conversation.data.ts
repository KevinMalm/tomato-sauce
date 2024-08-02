export type Role = 'user' | 'assistant' | 'system';


export interface ChatEntry {
    role: Role
    content: string
}

export interface ChatConversation {
    chats: ChatEntry[],
    inject_rag: boolean
}



export interface RagReference {
    content: string,
    distance: number
}

export interface RagLookup {
    context: string,
    lookups: RagReference[]
}