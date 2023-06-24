import { api } from "./configs/axiosConfig"
import { defineCancelApiObject } from "./configs/axiosUtils"
export const FilesApi = {
        listFilesAndFolders : async(path,cancel = false) => {
            const response = await api.request({
                url: "/file/",
                method: "GET",
                params: {
                    dir: path
                },
                signal: cancel ? cancelApiObject[this.listFilesAndFolders.name].handleRequestCancellation().signal : undefined,
            })
            return response.data
        },

        loadFileContent :  async(fileNameAndPath,cancel = false) => {
            const response = await api.request({
                url: "/file/content",
                method: "GET",
                params: {
                    file: fileNameAndPath
                },
                signal: cancel ? cancelApiObject[this.listFilesAndFolders.name].handleRequestCancellation().signal : undefined,
            })
            return response.data

        }
}

const cancelApiObject = defineCancelApiObject(FilesApi)