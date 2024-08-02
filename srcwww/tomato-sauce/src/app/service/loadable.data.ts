import { HttpClient } from "@angular/common/http";
import { RestResult, result_is_ok } from "../data/result.data";


export class Loadable<T> {

    error: string | null = null;
    data: T | null = null;
    loading: boolean = false;

    get is_loaded() {
        return this.data != null && this.loading == false;
    }

    get is_errored() {
        return this.data == null && this.loading == false;
    }

    with_loading(loading: boolean): Loadable<T> {
        this.loading = loading;
        return this;
    }

    _clear() {
        this.loading = true;
        this.data = null;
        this.error = null;
    }

    async set(http: HttpClient, builder: (client: HttpClient) => Promise<RestResult>) {
        try {

            this._clear();

            let response = await builder(http);
            if (result_is_ok(response)) {
                this.data = response.body as T
            } else {
                this.error = response.body as string
            }
            this.loading = false;
        } catch (e: Error | any) {
            this.data = null;
            this.error = e.message
            this.loading = false;
        }
    }

    async write(http: HttpClient, builder: (client: HttpClient, obj: T) => Promise<T>) {
        if (this.data == null) {
            return;
        }
        try {
            this.loading = true;
            this.error = null;
            this.data = await builder(http, this.data!);
            this.loading = false;
        } catch (e: Error | any) {
            this.data = null;
            this.error = (e.error?.error) ?? e.message;
            this.loading = false;
        }
    }

    static from_error<T>(message: string): Loadable<T> {
        let obj = new Loadable<T>();
        obj.error = message;
        return obj;
    }


}